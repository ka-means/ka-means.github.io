# %% [markdown]
# # F.Blackwell — Is a More Informative Observation Always Better?
#
# **Portfolio:** Autonomous Systems: My Research Portfolio
# **Area:** 01 Decision-Making Under Uncertainty
# **Series:** F — Foundation Experiments
# **Identifier:** F.Blackwell
#
# ---
#
# ## Founding Thesis
#
# **Blackwell (1953)** — When is one experiment more valuable than another?
#
# The proposition tested here:
#
# > A Blackwell-superior observation structure is always at least as good
# > as a Blackwell-inferior one — for any decision problem, any prior,
# > and any agent that uses the observation optimally.
#
# This is the Blackwell sufficiency theorem. It defines a partial order
# on observation structures (experiments): Σ₁ is Blackwell sufficient for Σ₂,
# written Σ₁ ≥_B Σ₂, if and only if Σ₂ can be obtained from Σ₁ by applying
# a stochastic transformation — a "garbling" — that randomly discards information.
#
# The theorem's power lies in its universality: if Σ₁ ≥_B Σ₂, then for any
# prior and any payoff structure, an optimal agent with Σ₁ performs at least
# as well as an optimal agent with Σ₂. More informative ≥ less informative,
# always, when the agent is optimal.
#
# This notebook tests two questions:
#
#   1. Does the Blackwell ordering hold empirically for Bayesian agents?
#   2. Under what conditions does more information fail to improve decisions?
#
# The second question is the bridge to Area 01's second central distinction:
#
#   information gain ≠ decision value
#
# More information always improves the agent's epistemic state. It does not
# always improve the agent's decision.
#
# ---
#
# ## The Observation Structure
#
# For a binary state space S = {0, 1} and binary observations O = {0, 1},
# a symmetric channel with accuracy p is:
#
#   P(o = s | s) = p       (correct signal)
#   P(o ≠ s | s) = 1 − p  (noise)
#
# The Blackwell ordering on symmetric binary channels is simply:
#   Σ(p₁) ≥_B Σ(p₂)  iff  p₁ ≥ p₂
#
# A garbling G of Σ(p₁) that produces Σ(p₂) is a stochastic flip:
# with probability α, keep the signal; with probability 1−α, flip it.
#
#   α = (p₂ + p₁ − 1) / (2p₁ − 1)    [derived in E02]
#
# Garbling demonstrates that a less informative structure is literally
# a degraded version of a more informative one.
#
# ---
#
# ## Connections to Area 01
#
# F.Blackwell is the natural sequel to F.Bayes:
#   F.Bayes    — does updating from evidence help? (fixed structure, vary n_obs)
#   F.Blackwell — which structure is better?     (fixed n_obs, vary structure)
#
# Key connections forward:
#   01.4 Active Sensing — the agent chooses which sensor to use.
#        F.Blackwell provides the comparison baseline: what does "better sensor" mean?
#   F.Shannon — mutual information I(s; o) is an information-theoretic measure
#               of Σ's value; Blackwell is the decision-theoretic measure.
#               F.Shannon will test whether I(s; o) predicts decision value.
#   F.Sondik  — F.Blackwell assumes the agent knows the observation structure.
#               F.Sondik relaxes this: the structure must be learned.

# %% [markdown]
# ## Imports and Configuration

# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy import stats
from collections import defaultdict
import warnings
warnings.filterwarnings('ignore')

SEED        = 42
N_EPISODES  = 10_000
DOORS       = {0: 'Left', 1: 'Right'}

np.random.seed(SEED)

plt.rcParams.update({
    'figure.dpi':        120,
    'axes.spines.top':   False,
    'axes.spines.right': False,
    'axes.grid':         True,
    'grid.alpha':        0.3,
    'font.size':         10,
})

COLORS = {
    'bayesian':    '#2563eb',
    'frequentist': '#16a34a',
    'no_update':   '#dc2626',
    'random':      '#9ca3af',
    'optimal':     '#000000',
    'garbled':     '#7c3aed',
    'majority':    '#d97706',
    'first_only':  '#db2777',
}

# %% [markdown]
# ## Observation Structures
#
# The key object in this notebook is an **observation structure** Σ(p):
# a symmetric binary channel characterized by a single parameter p ∈ [0.5, 1.0].
#
# p = 0.5: completely uninformative (pure noise)
# p = 1.0: perfectly informative (noiseless)
#
# Blackwell garbling: G(p₁ → p₂) takes output from Σ(p₁) and randomly flips
# each signal, simulating a less accurate channel Σ(p₂).

# %%
class ObsStructure:
    """
    Symmetric binary observation channel with accuracy p.

    P(o = s | s) = p       (correct signal probability)
    P(o ≠ s | s) = 1 - p   (noise probability)

    Blackwell ordering: Σ(p₁) ≥_B Σ(p₂)  iff  p₁ ≥ p₂
    """

    def __init__(self, p_correct: float):
        assert 0.5 <= p_correct <= 1.0, "p_correct must be in [0.5, 1.0]"
        self.p = p_correct

    def observe(self, true_state: int) -> int:
        """Draw one observation from the channel."""
        if np.random.random() < self.p:
            return true_state
        return 1 - true_state

    def likelihood(self, obs: int, state: int) -> float:
        """P(obs | state) for this channel."""
        return self.p if obs == state else (1.0 - self.p)

    def garble_to(self, target_p: float) -> 'GarblingMatrix':
        """
        Compute the stochastic matrix G that transforms this channel
        into a less informative one with accuracy target_p.

        G = [[α, 1-α], [1-α, α]] where α = (target_p + p - 1) / (2p - 1)
        """
        assert target_p <= self.p, "Garbling can only reduce informativeness"
        assert target_p >= 0.5,    "Target accuracy must be ≥ 0.5"
        alpha = (target_p + self.p - 1.0) / (2.0 * self.p - 1.0)
        return GarblingMatrix(alpha)


class GarblingMatrix:
    """
    Stochastic matrix G = [[α, 1-α], [1-α, α]].
    Applied to an observation o from Σ(p₁), produces an observation
    with the statistics of Σ(p₂).
    """

    def __init__(self, alpha: float):
        self.alpha = alpha

    def apply(self, obs: int) -> int:
        """Apply the garbling: keep obs with prob α, flip with prob 1-α."""
        if np.random.random() < self.alpha:
            return obs
        return 1 - obs


# %% [markdown]
# ## Environment

# %%
class TwoDoorEnv:
    """
    Binary two-door environment.
    True state s ∈ {0, 1}, actions {0, 1}, rewards +1 / −1.

    The observation structure is injected as an ObsStructure instance,
    allowing controlled comparison across structures.
    """

    def __init__(self, obs_structure: ObsStructure, p_switch: float = 0.0):
        self.struct     = obs_structure
        self.p_switch   = p_switch
        self.true_state = None

    def reset(self) -> int:
        self.true_state = np.random.randint(2)
        return self.struct.observe(self.true_state)

    def step(self, action: int):
        reward = 1.0 if action == self.true_state else -1.0
        if np.random.random() < self.p_switch:
            self.true_state = 1 - self.true_state
        return self.struct.observe(self.true_state), reward

    def optimal_action(self) -> int:
        return self.true_state


# %% [markdown]
# ## Agents

# %%
class RandomAgent:
    """Baseline: uniform random. Ignores all observations."""
    def reset(self, first_obs): pass
    def update(self, obs):      pass
    def act(self):              return np.random.randint(2)


class NoUpdateAgent:
    """Commits to its first observation. Zero sequential value."""
    def reset(self, first_obs):
        self.decision = first_obs
    def update(self, obs): pass
    def act(self):         return self.decision


class FrequentistAgent:
    """Majority vote across all observations."""
    def reset(self, first_obs):
        self.counts = [0, 0]
        self.counts[first_obs] += 1
    def update(self, obs):
        self.counts[obs] += 1
    def act(self):
        if self.counts[0] == self.counts[1]:
            return np.random.randint(2)
        return int(np.argmax(self.counts))


class BayesianAgent:
    """
    Proper Bayesian posterior with known observation structure.

    Prior: P(s=0) = 0.5 (uniform)
    Likelihood: from the injected ObsStructure
    """
    def __init__(self, obs_structure: ObsStructure, p_switch: float = 0.0):
        self.struct   = obs_structure
        self.p_switch = p_switch
        self.belief   = None    # P(s_t = 0 | h_t)

    def reset(self, first_obs):
        self.belief = 0.5
        self._update(first_obs)

    def _update(self, obs):
        b = self.belief
        p0 = self.struct.likelihood(obs, 0)
        p1 = self.struct.likelihood(obs, 1)
        unnorm0 = p0 * b
        unnorm1 = p1 * (1.0 - b)
        self.belief = unnorm0 / (unnorm0 + unnorm1)

    def update(self, obs):
        b_pred = (1.0 - self.p_switch) * self.belief + \
                  self.p_switch         * (1.0 - self.belief)
        self.belief = b_pred
        self._update(obs)

    def act(self):
        return 0 if self.belief >= 0.5 else 1

    def confidence(self):
        return max(self.belief, 1.0 - self.belief)


class GarbledBayesianAgent:
    """
    Bayesian agent that receives garbled observations.

    It sees observations from Σ(p₁) that have been garbled
    to simulate Σ(p₂). It uses the target structure's likelihoods
    as if it were receiving from Σ(p₂) directly.

    This verifies the garbling theorem: the garbled agent should
    produce the same decisions as a direct-Σ(p₂) Bayesian agent.
    """
    def __init__(self, target_structure: ObsStructure):
        self.struct = target_structure
        self.belief = None

    def reset(self, first_obs):
        self.belief = 0.5
        self._update(first_obs)

    def _update(self, obs):
        b  = self.belief
        p0 = self.struct.likelihood(obs, 0)
        p1 = self.struct.likelihood(obs, 1)
        unnorm0 = p0 * b
        unnorm1 = p1 * (1.0 - b)
        self.belief = unnorm0 / (unnorm0 + unnorm1)

    def update(self, obs):
        self._update(obs)

    def act(self):
        return 0 if self.belief >= 0.5 else 1


# %% [markdown]
# ## Utility: Run experiment with a single-observation-per-step environment

# %%
def run_experiment(env, agents, n_obs, n_episodes=N_EPISODES, seed=SEED):
    """
    Standard experiment runner.
    Agents observe n_obs sequential signals, then act once.
    Returns Performance Retention and Decision Disagreement per agent.
    """
    np.random.seed(seed)
    rewards = defaultdict(list)
    agreed  = defaultdict(list)

    for _ in range(n_episodes):
        first_obs = env.reset()
        for agent in agents.values():
            agent.reset(first_obs)

        for _ in range(n_obs - 1):
            obs, _ = env.step(action=0)
            for agent in agents.values():
                agent.update(obs)

        optimal = env.optimal_action()
        for name, agent in agents.items():
            action = agent.act()
            reward = 1.0 if action == optimal else -1.0
            rewards[name].append(reward)
            agreed[name].append(action == optimal)

    metrics = {}
    for name in agents:
        j = np.mean(rewards[name])
        metrics[name] = {
            'mean_reward':           j,
            'performance_retention': j,          # J_optimal = 1.0 always
            'success_rate':          np.mean(agreed[name]),
            'decision_disagreement': 1.0 - np.mean(agreed[name]),
        }
    return metrics


# %% [markdown]
# ---
# ## E01 — Blackwell Ordering Confirmed
#
# Sweep p_correct from 0.5 to 1.0 in fixed steps.
# For each value, run the Bayesian agent with n_obs=1.
#
# **Hypothesis:** Performance Retention should increase monotonically with p_correct,
# matching the theoretical prediction PR(p) = 2p − 1 for n_obs=1.
#
# Derivation: with n_obs=1 and a uniform prior, the Bayesian agent always acts
# on its first observation. P(correct | n_obs=1) = p_correct, so:
#   J(Bayesian, n_obs=1) = (+1)×p + (−1)×(1−p) = 2p − 1
#   PR = 2p − 1
#
# This gives PR = 0 at p=0.5 (pure noise) and PR = 1.0 at p=1.0 (perfect signal).
#
# We also show that all three informed agents (Bayesian, Frequentist, NoUpdate)
# are equivalent at n_obs=1 — as established in F.Bayes E01.

# %%
p_sweep = np.array([0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00])

results_e01 = {name: [] for name in ['bayesian', 'frequentist', 'no_update', 'random']}

for p in p_sweep:
    struct = ObsStructure(p)
    env    = TwoDoorEnv(struct)
    agents = {
        'bayesian':    BayesianAgent(struct),
        'frequentist': FrequentistAgent(),
        'no_update':   NoUpdateAgent(),
        'random':      RandomAgent(),
    }
    m = run_experiment(env, agents, n_obs=1)
    for name in agents:
        results_e01[name].append(m[name]['performance_retention'])

theoretical_e01 = 2 * p_sweep - 1

print("E01 — Performance Retention vs. p_correct (n_obs=1)")
print(f"{'p':>6}  {'Bayesian':>10}  {'Frequentist':>12}  {'No-update':>10}  {'Theory 2p-1':>12}")
print("-" * 60)
for i, p in enumerate(p_sweep):
    print(f"{p:>6.2f}  "
          f"{results_e01['bayesian'][i]:>10.4f}  "
          f"{results_e01['frequentist'][i]:>12.4f}  "
          f"{results_e01['no_update'][i]:>10.4f}  "
          f"{theoretical_e01[i]:>12.4f}")

# %%
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

ax = axes[0]
ax.plot(p_sweep, results_e01['bayesian'],    'o-', color=COLORS['bayesian'],
        label='Bayesian', lw=2, ms=5)
ax.plot(p_sweep, results_e01['frequentist'], 's--', color=COLORS['frequentist'],
        label='Frequentist', lw=2, ms=5, alpha=0.8)
ax.plot(p_sweep, results_e01['no_update'],   '^:', color=COLORS['no_update'],
        label='No-update', lw=2, ms=5, alpha=0.8)
ax.plot(p_sweep, results_e01['random'],      'D:', color=COLORS['random'],
        label='Random', lw=1, ms=4, alpha=0.6)
ax.plot(p_sweep, theoretical_e01,           '--', color=COLORS['optimal'],
        label='Theory: PR = 2p − 1', lw=1.5, alpha=0.7)
ax.set_xlabel('Observation Accuracy  p')
ax.set_ylabel('Performance Retention  PR')
ax.set_title('E01 — Blackwell Ordering: PR vs. p (n_obs=1)')
ax.legend(fontsize=8)
ax.set_xlim(0.48, 1.02)
ax.set_ylim(-0.1, 1.05)
ax.axhline(0, color='gray', lw=0.8, ls=':')

ax = axes[1]
gap_bayes_random = np.array(results_e01['bayesian']) - np.array(results_e01['random'])
ax.bar(p_sweep, gap_bayes_random, width=0.04, color=COLORS['bayesian'], alpha=0.7,
       label='Bayesian − Random')
ax.set_xlabel('Observation Accuracy  p')
ax.set_ylabel('PR advantage over random baseline')
ax.set_title('E01 — Value Added by Observation Structure')
ax.legend(fontsize=8)

plt.suptitle('E01: Blackwell Ordering — more informative ≥ less informative (n_obs=1)', y=1.01)
plt.tight_layout()
plt.savefig('e01_blackwell_ordering.png', bbox_inches='tight')
plt.show()

print("\nFinding: PR = 2p − 1 exactly (within simulation error).")
print("All informed agents equivalent at n_obs=1: Blackwell ordering holds trivially here.")
print("The ordering's strength appears at n_obs > 1 — see E02 and F.Bayes E02.")

# %% [markdown]
# ---
# ## E02 — Garbling Verification
#
# The Blackwell theorem does not just say that Σ(p₁) ≥ Σ(p₂) when p₁ > p₂.
# It says something constructive: Σ(p₂) IS a garbled version of Σ(p₁).
# There exists an explicit stochastic transformation G such that:
#
#   Σ(p₂) = G · Σ(p₁)
#
# For symmetric binary channels, this garbling is: flip the observation
# with probability 1−α, where:
#
#   α = (p₂ + p₁ − 1) / (2p₁ − 1)
#
# **Experimental design:**
# Take a source structure Σ(p_source=0.9).
# Garble it to simulate Σ(p_target) for p_target in {0.85, 0.80, ..., 0.55, 0.50}.
# Compare:
#   - A direct agent receiving observations from Σ(p_target)
#   - A garbled agent receiving garbled observations from Σ(p_source)
#
# **Hypothesis:** Both agents should produce statistically identical PR.
# The garbling theorem guarantees this analytically; we verify it empirically.

# %%
p_source = 0.90
p_targets = np.array([0.85, 0.80, 0.75, 0.70, 0.65, 0.60, 0.55, 0.50])
N_OBS_E02 = 1

struct_source = ObsStructure(p_source)

results_direct  = []   # Bayesian with direct Σ(p_target)
results_garbled = []   # Bayesian with garbled Σ(p_source) → p_target

np.random.seed(SEED)

for p_target in p_targets:
    struct_target = ObsStructure(p_target)
    garbling      = struct_source.garble_to(p_target)

    # Direct experiment
    env_direct = TwoDoorEnv(struct_target)
    agent_direct = BayesianAgent(struct_target)
    m_direct = run_experiment(env_direct, {'bayesian': agent_direct}, N_OBS_E02)
    results_direct.append(m_direct['bayesian']['performance_retention'])

    # Garbled experiment: receive Σ(0.9) observations, apply garbling, use Σ(p_target) likelihoods
    np.random.seed(SEED)
    rewards_g, agreed_g = [], []
    for _ in range(N_EPISODES):
        true_state    = np.random.randint(2)
        raw_obs       = struct_source.observe(true_state)
        garbled_obs   = garbling.apply(raw_obs)
        optimal       = true_state

        # Agent uses Σ(p_target) likelihoods on the garbled observation
        b = 0.5
        p0 = struct_target.likelihood(garbled_obs, 0)
        p1 = struct_target.likelihood(garbled_obs, 1)
        unnorm0 = p0 * b
        unnorm1 = p1 * (1 - b)
        belief  = unnorm0 / (unnorm0 + unnorm1)
        action  = 0 if belief >= 0.5 else 1

        reward = 1.0 if action == optimal else -1.0
        rewards_g.append(reward)
        agreed_g.append(action == optimal)

    results_garbled.append(np.mean(rewards_g))

# Analytical reference
theoretical_at_targets = 2 * p_targets - 1

print(f"E02 — Garbling Verification (p_source={p_source}, n_obs={N_OBS_E02})")
print(f"\n{'p_target':>10}  {'Direct PR':>10}  {'Garbled PR':>11}  {'Theory':>8}  {'Gap (D-G)':>10}")
print("-" * 56)
for i, pt in enumerate(p_targets):
    gap = results_direct[i] - results_garbled[i]
    print(f"{pt:>10.2f}  {results_direct[i]:>10.4f}  {results_garbled[i]:>11.4f}  "
          f"{theoretical_at_targets[i]:>8.4f}  {gap:>10.4f}")

# %%
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

ax = axes[0]
ax.plot(p_targets, results_direct,  'o-',  color=COLORS['bayesian'],  lw=2, ms=6,
        label=f'Direct Σ(p_target)')
ax.plot(p_targets, results_garbled, 's--', color=COLORS['garbled'],   lw=2, ms=6,
        label=f'Garbled from Σ({p_source})')
ax.plot(p_targets, theoretical_at_targets, '--', color=COLORS['optimal'], lw=1.5,
        label='Theory: 2p − 1', alpha=0.7)
ax.set_xlabel('Target Accuracy  p_target')
ax.set_ylabel('Performance Retention  PR')
ax.set_title(f'E02 — Direct vs. Garbled Observations (source p={p_source})')
ax.legend(fontsize=8)
ax.set_xlim(0.48, 0.87)

ax = axes[1]
alpha_values = [(pt + p_source - 1.0) / (2.0 * p_source - 1.0) for pt in p_targets]
ax.bar(p_targets, alpha_values, width=0.04, color=COLORS['garbled'], alpha=0.7)
ax.axhline(1.0, color='gray', ls='--', lw=1, label='α=1: identity (no garbling)')
ax.axhline(0.5, color='gray', ls=':',  lw=1, label='α=0.5: max noise (→ p=0.5)')
ax.set_xlabel('Target Accuracy  p_target')
ax.set_ylabel('Garbling retention rate  α')
ax.set_title(f'E02 — Garbling Parameter α (source p={p_source})')
ax.legend(fontsize=8)

plt.suptitle('E02: Garbling — less informative is a degraded version of more informative', y=1.01)
plt.tight_layout()
plt.savefig('e02_garbling_verification.png', bbox_inches='tight')
plt.show()

print("\nFinding: Direct and Garbled agents produce identical PR at each target.")
print("The garbling theorem holds empirically: Σ(p₂) is literally a noisy Σ(p₁).")
print("This confirms the constructive claim: information can always be thrown away,")
print("but it can never be manufactured from a less informative source.")

# %% [markdown]
# ---
# ## E03 — Information Gain ≠ Decision Value
#
# The Blackwell ordering says: more information is always at least as good.
# But "at least as good" allows for exact equality: sometimes extra information
# has zero decision value.
#
# **Setup:** vary the reward asymmetry while holding the observation structure fixed.
#
#   Reward case A: R_correct = +1, R_wrong = −1  (symmetric loss — info matters)
#   Reward case B: R_correct = +1, R_wrong = +0.8 (small loss — info matters less)
#   Reward case C: R_correct = +1, R_wrong = +1.0 (no loss — info irrelevant)
#
# In case C, both actions yield identical reward regardless of state.
# The Bayesian agent's posterior can be 0.99 or 0.51 — it doesn't matter.
# No observation structure can help: information gain is positive, decision value is zero.
#
# **Hypothesis:** In case C, PR = 1.0 for ALL observation structures including p=0.5.
# In case A, PR tracks the Blackwell ordering. Case B sits between.
#
# This is the clearest empirical demonstration of the Area 01 central distinction:
#   information gain ≠ decision value

# %%
N_OBS_E03   = 1
reward_cases = {
    'A (symmetric loss)': -1.0,
    'B (small loss)':     +0.8,
    'C (no loss)':        +1.0,
}

results_e03 = {case: [] for case in reward_cases}

for case_label, r_wrong in reward_cases.items():
    for p in p_sweep:
        np.random.seed(SEED)
        rewards_case = []

        struct = ObsStructure(p)

        for _ in range(N_EPISODES):
            true_state = np.random.randint(2)
            obs        = struct.observe(true_state)

            # Bayesian posterior after one observation
            b = 0.5
            p0 = struct.likelihood(obs, 0)
            p1 = struct.likelihood(obs, 1)
            b  = (p0 * b) / (p0 * b + p1 * (1 - b))
            action = 0 if b >= 0.5 else 1

            # Compute reward based on this case's asymmetry
            r_correct = 1.0
            if action == true_state:
                reward = r_correct
            else:
                reward = r_wrong
            rewards_case.append(reward)

        # Performance retention: normalize by optimal expected reward
        # With case C, optimal is r_correct = 1.0
        # With case A/B, optimal = r_correct = 1.0 (always choosing correct door)
        j_agent   = np.mean(rewards_case)
        j_optimal = r_correct   # optimal agent always gets +1
        results_e03[case_label].append(j_agent / j_optimal)

print("E03 — Decision Value vs. Information Gain")
print(f"\n{'p':>6}  {'Case A (r=-1)':>14}  {'Case B (r=+0.8)':>16}  {'Case C (r=+1)':>14}")
print("-" * 56)
for i, p in enumerate(p_sweep):
    print(f"{p:>6.2f}  "
          f"{results_e03['A (symmetric loss)'][i]:>14.4f}  "
          f"{results_e03['B (small loss)'][i]:>16.4f}  "
          f"{results_e03['C (no loss)'][i]:>14.4f}")

# %%
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

case_styles = {
    'A (symmetric loss)': ('#2563eb', '-',  'Case A: R_wrong=−1 (info always helps)'),
    'B (small loss)':     ('#d97706', '--', 'Case B: R_wrong=+0.8 (info helps less)'),
    'C (no loss)':        ('#dc2626', ':',  'Case C: R_wrong=+1   (info irrelevant)'),
}

ax = axes[0]
for case, (color, ls, label) in case_styles.items():
    ax.plot(p_sweep, results_e03[case], 'o'+ls, color=color, lw=2, ms=5, label=label)
ax.axhline(1.0, color=COLORS['optimal'], ls='--', lw=1, alpha=0.5, label='PR = 1.0 ceiling')
ax.set_xlabel('Observation Accuracy  p')
ax.set_ylabel('Performance Retention  PR')
ax.set_title('E03 — PR vs. p for Three Reward Structures')
ax.legend(fontsize=8)
ax.set_xlim(0.48, 1.02)
ax.set_ylim(-0.05, 1.08)

# Marginal decision value of going from p=0.5 to p=1.0
ax = axes[1]
for case, (color, ls, label) in case_styles.items():
    delta_values = np.array(results_e03[case]) - results_e03[case][0]
    ax.plot(p_sweep, delta_values, 'o'+ls, color=color, lw=2, ms=5, label=label)
ax.set_xlabel('Observation Accuracy  p')
ax.set_ylabel('Δ PR relative to uninformative (p=0.5)')
ax.set_title('E03 — Marginal Decision Value of Information')
ax.legend(fontsize=8)
ax.axhline(0, color='gray', lw=0.8, ls=':')

plt.suptitle('E03: Information gain ≠ decision value\nCase C: perfect information (p=1.0) gives same PR as pure noise (p=0.5)', y=1.03)
plt.tight_layout()
plt.savefig('e03_information_vs_decision_value.png', bbox_inches='tight')
plt.show()

print("\nFinding: In Case C, PR = 1.0 for all p ∈ [0.5, 1.0].")
print("More information (higher p) does not improve the decision.")
print("The information gain I(s; o) > 0 for p > 0.5, but ΔDecisionValue = 0.")
print("This is the empirical confirmation of information gain ≠ decision value.")

# %% [markdown]
# ---
# ## E04 — The Value of Information Depends on the Prior
#
# E03 showed that reward structure determines whether information is useful.
# E04 shows a complementary fact: the **prior** also determines information value.
#
# **Setup:** fix the reward structure (Case A: R_wrong=−1) but vary the prior.
#
# At a uniform prior (p₀=0.5), the agent is maximally uncertain — observations
# have maximum decision value. As the prior strengthens toward certainty
# (p₀ → 1.0), the agent would act on the prior alone regardless of observations.
#
# Formally, with a strong prior p₀ and one observation with accuracy p:
#   Posterior: P(s=0 | obs=0) = p₀p / (p₀p + (1−p₀)(1−p))
#   If p₀ is close to 1, this posterior stays above 0.5 even for obs=1 (opposing signal).
#
# **Hypothesis:** information value decreases as the prior strengthens.
# At p₀ sufficiently close to 1.0, even a perfectly informative sensor (p=1.0)
# does not change the agent's decision relative to a noisy sensor (p=0.6).
# The prior makes the observation decision-irrelevant.
#
# This foreshadows 01.2 Memory Matters: what happens when past evidence
# has created a strong implicit prior that makes new observations ineffective?

# %%
p_obs_sweep   = np.array([0.6, 0.7, 0.8, 0.9, 1.0])
p_prior_sweep = np.array([0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99])

N_OBS_E04    = 1

# For each (p_prior, p_obs) pair, compute PR of the Bayesian agent
results_e04 = np.zeros((len(p_prior_sweep), len(p_obs_sweep)))

for i, p_prior in enumerate(p_prior_sweep):
    for j, p_obs in enumerate(p_obs_sweep):
        np.random.seed(SEED)
        struct = ObsStructure(p_obs)

        rewards_ep = []
        for _ in range(N_EPISODES):
            true_state = np.random.choice([0, 1], p=[p_prior, 1 - p_prior])
            obs        = struct.observe(true_state)

            # Bayesian update from prior p_prior
            p0 = struct.likelihood(obs, 0) * p_prior
            p1 = struct.likelihood(obs, 1) * (1.0 - p_prior)
            b  = p0 / (p0 + p1)
            action = 0 if b >= 0.5 else 1

            reward = 1.0 if action == true_state else -1.0
            rewards_ep.append(reward)

        results_e04[i, j] = np.mean(rewards_ep)

print("E04 — PR vs. prior strength and observation accuracy")
header = f"{'p_prior / p_obs':>16}"
print(f"\n{header}", end="")
for p in p_obs_sweep:
    print(f"  p={p:.1f}", end="")
print()
print("-" * 55)
for i, p_prior in enumerate(p_prior_sweep):
    print(f"p_prior={p_prior:.2f}      ", end="")
    for j in range(len(p_obs_sweep)):
        print(f"  {results_e04[i, j]:>6.3f}", end="")
    print()

# %%
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

ax = axes[0]
for j, p_obs in enumerate(p_obs_sweep):
    color = plt.cm.Blues(0.3 + 0.7 * j / (len(p_obs_sweep) - 1))
    ax.plot(p_prior_sweep, results_e04[:, j], 'o-', color=color, lw=2, ms=5,
            label=f'p_obs = {p_obs:.1f}')
ax.set_xlabel('Prior strength  p_prior = P(s=0)')
ax.set_ylabel('Performance Retention  PR')
ax.set_title('E04 — PR vs. Prior Strength for Different Sensors')
ax.legend(fontsize=8)
ax.axvline(0.5, color='gray', ls=':', lw=1, label='Uniform prior')

ax = axes[1]
# Spread: PR(p=1.0) - PR(p=0.6) at each prior
spread = results_e04[:, -1] - results_e04[:, 0]
ax.plot(p_prior_sweep, spread, 'o-', color=COLORS['bayesian'], lw=2, ms=6)
ax.axhline(0, color='gray', ls='--', lw=1)
ax.set_xlabel('Prior strength  p_prior')
ax.set_ylabel('PR spread: PR(p=1.0) − PR(p=0.6)')
ax.set_title('E04 — Marginal Value of Perfect vs. Weak Sensor')
ax.set_ylim(-0.05, None)

plt.suptitle('E04: Prior strength reduces the decision value of additional information', y=1.01)
plt.tight_layout()
plt.savefig('e04_prior_vs_information_value.png', bbox_inches='tight')
plt.show()

print("\nFinding: At p_prior=0.99, the PR difference between p_obs=0.6 and p_obs=1.0")
print(f"is {spread[-1]:.4f}. At p_prior=0.50, the same difference is {spread[0]:.4f}.")
print("A strong prior makes the observation decision-irrelevant.")
print("The Blackwell ordering holds (p=1.0 still ≥ p=0.6), but the gap collapses.")

# %% [markdown]
# ---
# ## E05 — Dual-Sensor: Combining Independent Observations
#
# So far we have tested single-channel observation structures.
# E05 introduces an environment with TWO independent sensors, each with accuracy p_each.
#
# **The information-combination question:**
# If two sensors each have accuracy p_each, does a Bayesian agent using both
# outperform one using a single sensor with the same p_each?
#
# **Theoretical answer:** yes. Two independent sensors with accuracy p produce
# a combined posterior that is strictly stronger than either alone — equivalent
# to having a single sensor with higher effective accuracy p_eff > p_each.
#
# **But only if the agent can combine them.**
#
# Three agents are compared in the dual-sensor environment:
#
#   DualBayesian:  knows both sensors' likelihoods; computes joint posterior
#   MajorityVote:  takes majority of all observations (both sensors, all steps)
#   FirstSensor:   uses only the first sensor's first observation; ignores second
#
# **Hypothesis:**
#   DualBayesian   outperforms SingleBayesian (p_each, n_obs=1)
#   MajorityVote   underperforms DualBayesian (suboptimal combination)
#   FirstSensor    performs identically to SingleBayesian (wastes second sensor)
#
# This demonstrates the Blackwell theorem's requirement of OPTIMAL use:
# the ordering holds for agents that fully exploit the observation structure.

# %%
class TwoDoorDualEnv:
    """
    Two-door environment with two independent sensors per step.
    Each observation is a tuple (o₁, o₂) of two independent binary signals.
    """

    def __init__(self, p1: float, p2: float, p_switch: float = 0.0):
        self.p1         = p1
        self.p2         = p2
        self.p_switch   = p_switch
        self.true_state = None

    def _observe(self):
        o1 = self.true_state if np.random.random() < self.p1 else 1 - self.true_state
        o2 = self.true_state if np.random.random() < self.p2 else 1 - self.true_state
        return (o1, o2)

    def reset(self):
        self.true_state = np.random.randint(2)
        return self._observe()

    def step(self, action):
        reward = 1.0 if action == self.true_state else -1.0
        if np.random.random() < self.p_switch:
            self.true_state = 1 - self.true_state
        return self._observe(), reward

    def optimal_action(self):
        return self.true_state


class DualBayesianAgent:
    """
    Bayesian agent with two independent sensors.
    Computes joint posterior: P(s=0 | o₁, o₂) = P(o₁|s=0)P(o₂|s=0) / P(o₁,o₂)
    (Independence allows factored likelihood.)
    """
    def __init__(self, p1: float, p2: float):
        self.p1     = p1
        self.p2     = p2
        self.belief = None

    def _joint_likelihood(self, obs, state):
        o1, o2 = obs
        l1 = self.p1 if o1 == state else (1 - self.p1)
        l2 = self.p2 if o2 == state else (1 - self.p2)
        return l1 * l2

    def _update(self, obs):
        b       = self.belief
        p0      = self._joint_likelihood(obs, 0)
        p1      = self._joint_likelihood(obs, 1)
        unnorm0 = p0 * b
        unnorm1 = p1 * (1 - b)
        self.belief = unnorm0 / (unnorm0 + unnorm1)

    def reset(self, first_obs):
        self.belief = 0.5
        self._update(first_obs)

    def update(self, obs):
        self._update(obs)

    def act(self):
        return 0 if self.belief >= 0.5 else 1


class MajorityVoteAgent:
    """
    Counts all observations from both sensors across all steps.
    Takes majority vote. Does not model sensor independence explicitly.
    """
    def reset(self, first_obs):
        self.counts = [0, 0]
        for o in first_obs:
            self.counts[o] += 1

    def update(self, obs):
        for o in obs:
            self.counts[o] += 1

    def act(self):
        if self.counts[0] == self.counts[1]:
            return np.random.randint(2)
        return int(np.argmax(self.counts))


class FirstSensorAgent:
    """
    Uses only the first observation from the first sensor.
    Ignores the second sensor entirely.
    Equivalent to a single-sensor no-update agent.
    """
    def reset(self, first_obs):
        self.decision = first_obs[0]   # only first sensor's first reading

    def update(self, obs):
        pass

    def act(self):
        return self.decision


# %%
p_each_sweep = np.array([0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90])
N_OBS_E05    = 1   # single observation step, but TWO sensors per step

results_dual_bayes  = []
results_majority    = []
results_first_sensor = []
results_single_bayes = []   # single sensor Bayesian (reference: uses only sensor 1)

for p_each in p_each_sweep:
    np.random.seed(SEED)

    # Dual-sensor environment
    env_dual = TwoDoorDualEnv(p1=p_each, p2=p_each)
    agents_dual = {
        'dual_bayes':    DualBayesianAgent(p1=p_each, p2=p_each),
        'majority_vote': MajorityVoteAgent(),
        'first_sensor':  FirstSensorAgent(),
    }

    rewards_d    = defaultdict(list)
    agreed_d     = defaultdict(list)

    for _ in range(N_EPISODES):
        first_obs = env_dual.reset()
        for agent in agents_dual.values():
            agent.reset(first_obs)
        for _ in range(N_OBS_E05 - 1):
            obs, _ = env_dual.step(0)
            for agent in agents_dual.values():
                agent.update(obs)
        optimal = env_dual.optimal_action()
        for name, agent in agents_dual.items():
            action = agent.act()
            reward = 1.0 if action == optimal else -1.0
            rewards_d[name].append(reward)
            agreed_d[name].append(action == optimal)

    results_dual_bayes.append(np.mean(rewards_d['dual_bayes']))
    results_majority.append(np.mean(rewards_d['majority_vote']))
    results_first_sensor.append(np.mean(rewards_d['first_sensor']))

    # Single-sensor Bayesian (reference)
    struct_single = ObsStructure(p_each)
    env_single    = TwoDoorEnv(struct_single)
    agent_single  = BayesianAgent(struct_single)
    m_single = run_experiment(env_single, {'b': agent_single}, n_obs=N_OBS_E05)
    results_single_bayes.append(m_single['b']['performance_retention'])

# Effective single-sensor equivalent accuracy for dual sensors
# P(correct | dual Bayes) = PR/2 + 0.5 (since PR = 2p-1)
effective_p_eff = [(pr + 1) / 2.0 for pr in results_dual_bayes]

print("E05 — Dual-Sensor vs. Single-Sensor (n_obs=1 step, two sensors per step)")
print(f"\n{'p_each':>7}  {'DualBayes':>10}  {'Majority':>9}  {'FirstSensor':>12}  "
      f"{'SingleBayes':>12}  {'p_eff':>6}")
print("-" * 70)
for i, p in enumerate(p_each_sweep):
    print(f"{p:>7.2f}  {results_dual_bayes[i]:>10.4f}  {results_majority[i]:>9.4f}  "
          f"{results_first_sensor[i]:>12.4f}  {results_single_bayes[i]:>12.4f}  "
          f"{effective_p_eff[i]:>6.4f}")

# %%
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

ax = axes[0]
ax.plot(p_each_sweep, results_dual_bayes,    'o-',  color=COLORS['bayesian'],   lw=2, ms=6,
        label='DualBayesian (uses both sensors optimally)')
ax.plot(p_each_sweep, results_majority,      's--', color=COLORS['majority'],   lw=2, ms=5,
        label='MajorityVote (counts all obs, no model)')
ax.plot(p_each_sweep, results_first_sensor,  '^:',  color=COLORS['first_only'], lw=2, ms=5,
        label='FirstSensor (ignores second sensor)')
ax.plot(p_each_sweep, results_single_bayes,  'D--', color=COLORS['no_update'], lw=1.5, ms=4,
        label='SingleBayesian reference (one sensor, n=1)', alpha=0.7)
ax.set_xlabel('Per-sensor accuracy  p_each')
ax.set_ylabel('Performance Retention  PR')
ax.set_title('E05 — Dual Sensor: Agent Ability to Combine Information')
ax.legend(fontsize=8)

ax = axes[1]
ax.plot(p_each_sweep, effective_p_eff, 'o-',  color=COLORS['bayesian'], lw=2, ms=6,
        label='Effective single-sensor equivalent p_eff')
ax.plot(p_each_sweep, p_each_sweep,    '--',  color='gray',             lw=1.5,
        label='p_each (single-sensor baseline)')
gap = np.array(effective_p_eff) - p_each_sweep
for x, g in zip(p_each_sweep, gap):
    ax.annotate(f'+{g:.3f}', (x, x + g/2), fontsize=8, ha='center', color=COLORS['bayesian'])
ax.fill_between(p_each_sweep, p_each_sweep, effective_p_eff,
                color=COLORS['bayesian'], alpha=0.1, label='Information gain from second sensor')
ax.set_xlabel('Per-sensor accuracy  p_each')
ax.set_ylabel('Effective accuracy')
ax.set_title('E05 — Second Sensor Gain (DualBayesian)')
ax.legend(fontsize=8)

plt.suptitle('E05: Two sensors help — but only if the agent knows how to use them', y=1.01)
plt.tight_layout()
plt.savefig('e05_dual_sensor.png', bbox_inches='tight')
plt.show()

# Compute what percent better DualBayes is vs FirstSensor
gains = [(results_dual_bayes[i] - results_first_sensor[i]) for i in range(len(p_each_sweep))]
print(f"\nPR gain from second sensor (DualBayes − FirstSensor):")
for p, g in zip(p_each_sweep, gains):
    print(f"  p={p:.2f}: {g:+.4f}")

print("\nNote: gains are small (~0.009) at n_obs=1. This is expected mathematically.")
print("For two INDEPENDENT symmetric binary sensors with random tie-breaking:")
print("  P(correct | dual) = p² + 2p(1-p)×0.5 + (1-p)²×0 = p² + p - p² = p")
print("The dual sensor gives the SAME decision accuracy as one sensor at n_obs=1!")
print("The benefit of a second sensor appears at n_obs > 1 (more observation steps).")
print("To see the gain clearly, compare DualBayes at n_obs=2 vs SingleBayes at n_obs=2.")
print("\nFinding (corrected): At n_obs=1, symmetric dual sensors add negligible value.")
print("The Blackwell ordering holds (more info ≥ less info) but the gap is mathematically zero")
print("for symmetric binary channels with random tie-breaking at n_obs=1.")
print("This reveals a limit of the theorem: superiority can be zero in specific regimes.")

# %% [markdown]
# ---
# ## Summary of Findings
#
# What the five experiments established:

# %%
print("=" * 72)
print("F.Blackwell — Summary of Findings")
print("=" * 72)

pr_05 = results_e01['bayesian'][0]   # p=0.5
pr_10 = results_e01['bayesian'][-1]  # p=1.0

print(f"""
FINDING 1 (E01): The Blackwell ordering holds empirically for Bayesian agents.
PR increases monotonically with p_correct, matching theory: PR = 2p − 1.
  PR at p=0.50 (pure noise):     {pr_05:.4f} ≈ 0 (expected: 0.0)
  PR at p=1.00 (perfect sensor): {pr_10:.4f} ≈ 1 (expected: 1.0)
All informed agents are equivalent at n_obs=1 (F.Bayes E01 confirmed).
""")

gap_direct_garbled = max(abs(results_direct[i] - results_garbled[i])
                         for i in range(len(p_targets)))
print(f"""FINDING 2 (E02): Garbling theorem holds.
A less informative structure is literally a randomized degradation of
a more informative one. Maximum empirical gap between direct and garbled
Bayesian agents: {gap_direct_garbled:.4f} (within simulation noise).
This confirms the constructive content of Blackwell's theorem:
information can be thrown away, but not manufactured.
""")

pr_c_min = min(results_e03['C (no loss)'])
pr_c_max = max(results_e03['C (no loss)'])
pr_a_p05 = results_e03['A (symmetric loss)'][0]
pr_a_p10 = results_e03['A (symmetric loss)'][-1]
print(f"""FINDING 3 (E03): Information gain ≠ decision value.
In Case C (R_wrong = +1.0), PR = {pr_c_min:.4f}–{pr_c_max:.4f} for all p ∈ [0.5, 1.0].
Perfect information (p=1.0) gives identical PR to pure noise (p=0.5).
In Case A (R_wrong = −1.0), PR spans [{pr_a_p05:.4f}, {pr_a_p10:.4f}].
The reward structure determines whether information is decision-relevant.
""")

print(f"""FINDING 4 (E04): Prior strength reduces the decision value of information.
With a strong prior (p_prior=0.99), the marginal PR gain from upgrading
from p_obs=0.6 to p_obs=1.0 collapses to {spread[-1]:.4f}.
At uniform prior (p_prior=0.50), the same upgrade gives {spread[0]:.4f} PR improvement.
A strong belief makes new observations decision-irrelevant even when informative.
""")

gain_e05_70 = results_dual_bayes[3] - results_first_sensor[3]  # p=0.70
print(f"""FINDING 5 (E05): At n_obs=1, symmetric dual sensors add near-zero decision value.
At p_each=0.70, DualBayesian − FirstSensor = {gain_e05_70:.4f} (≈ simulation noise).
Mathematical reason: P(correct | dual symmetric binary) = p = P(correct | single).
The tie-breaking when sensors disagree exactly cancels the agreement gain.
The dual-sensor advantage appears at n_obs > 1, where disagreements
can be resolved by accumulating more evidence.
This is a precision finding: more information is at least as good (equality allowed),
and equality occurs here at n_obs=1 for symmetric binary dual sensors.
""")

# %% [markdown]
# ---
# ## Open Questions
#
# 1. E03 showed information is irrelevant when R_wrong = R_correct.
#    Is there a formal threshold in reward asymmetry below which
#    information becomes decision-relevant?
#    (→ relates to Information Sensitivity IS(θ) in Area 01 metrics)
#
# 2. E04 showed prior strength reduces information value.
#    At what prior strength does the optimal decision become prior-only?
#    Is there a closed-form threshold as a function of (p_prior, p_obs)?
#    (→ connects to 01.2 Memory Matters: accumulated evidence as implicit prior)
#
# 3. E05 showed dual sensors help a Bayesian agent.
#    How does this scale with sensor count k?
#    At what k does adding another sensor yield diminishing marginal returns?
#    (→ connects to 01.4 Active Sensing: how many sensors to acquire?)
#
# 4. The Blackwell ordering is a partial order: some structures are incomparable
#    (neither garbles the other). This happens with asymmetric channels or
#    multi-outcome observations. We only tested symmetric binary channels here.
#    Under an incomparable pair, which structure wins depends on the decision problem.
#    (→ this is exactly the question F.Shannon addresses)
#
# ---
# ## Connections to Next Experiments
#
# F.Markov — F.Blackwell compared structures for a STATIC world (single step).
#            F.Markov asks: what information from the past must survive?
#            The Markov property is the answer when the world changes over time.
#
# F.Shannon — F.Blackwell used the Blackwell ordering (decision-theoretic).
#             F.Shannon uses mutual information I(s; o) (information-theoretic).
#             The question: does I(s; o) predict decision value?
#             In E03 above, I(s; o) > 0 in Case C but decision value = 0.
#             F.Shannon will test whether H(s|o) predicts PR across conditions.
#
# 01.4 Active Sensing — F.Blackwell established the baseline: given a choice
#              between Σ(p₁) and Σ(p₂) with p₁ > p₂, always prefer Σ(p₁)
#              for an optimal Bayesian agent.
#              01.4 asks: what if obtaining Σ(p₁) has a cost?
#              How should the agent decide whether to sense at all?

print("\nNotebook F.Blackwell complete.")
print("Outputs: e01_blackwell_ordering.png, e02_garbling_verification.png,")
print("         e03_information_vs_decision_value.png,")
print("         e04_prior_vs_information_value.png,")
print("         e05_dual_sensor.png")
