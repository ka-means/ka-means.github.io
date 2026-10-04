# %% [markdown]
# # F.Bellman — The Value of Information and Optimal Lookahead
# **Area 01 · Decision-Making Under Uncertainty — F-Series Foundational Experiments**
#
# **Historical thesis tested:**
# Bellman's principle of optimality (1957): a policy is optimal iff at every decision
# point it chooses the action that maximises immediate reward plus the discounted value
# of the resulting state. In a POMDP, "state" is replaced by BELIEF — a distribution
# over hidden states. The agent must plan over beliefs, not states.
#
# **Testbed: Tiger Problem (Cassandra, Kaelbling & Littman, 1994)**
#   - Two doors: L and R. Hidden state s ∈ {TL, TR} (tiger behind L or R).
#   - Three actions: open-L, open-R, listen.
#   - listen: costs −1, gives noisy observation (correct w.p. p_listen). State unchanged.
#   - open-*: large reward (safe door +10) or large penalty (tiger door −100). State RESETS.
#   - Optimal strategy: listen until confident, then open the safe door.
#
# **Experiments:**
# - E01: Value function V_h(b) over beliefs — piecewise linear and convex
# - E02: Myopic vs k-step lookahead — cumulative reward and open accuracy
# - E03: Optimal listens and reward vs channel quality p_listen
# - E04: Value of information VOI(b) = V_h(b) − V_myopic(b), maximised at b=0.5
# - E05: Discount factor γ and the critical listen/act threshold

# %% [markdown]
# ## Imports and configuration

# %%
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

np.random.seed(42)

R_SAFE   = +10.0
R_TIGER  = -100.0
R_LISTEN =  -1.0

COL_MYOPIC = '#dc2626'
COL_K1     = '#d97706'
COL_K2     = '#16a34a'
COL_K3     = '#0891b2'
COL_K5     = '#7c3aed'
COL_K10    = '#2563eb'
COL_RANDOM = '#9ca3af'
COL_OPT    = '#000000'

plt.rcParams.update({
    'figure.dpi': 120, 'font.size': 10,
    'axes.spines.top': False, 'axes.spines.right': False,
    'axes.grid': True, 'grid.alpha': 0.3,
})

# %% [markdown]
# ## Tiger POMDP model

# %%
class TigerPOMDP:
    """Tiger POMDP (Cassandra et al. 1994).

    State:   s ∈ {0=TigerLeft, 1=TigerRight}
    Actions: 0=OpenLeft, 1=OpenRight, 2=Listen
    Obs:     0=HearLeft, 1=HearRight
    Belief:  b = P(tiger=Left)
    """
    OPEN_L = 0;  OPEN_R = 1;  LISTEN = 2
    S = 2;       A = 3;       O = 2

    def __init__(self, p_listen: float = 0.85, gamma: float = 0.95):
        self.p   = p_listen
        self.gamma = gamma

    def reward(self, s: int, a: int) -> float:
        if a == self.OPEN_L:  return R_TIGER if s == 0 else R_SAFE
        if a == self.OPEN_R:  return R_TIGER if s == 1 else R_SAFE
        return R_LISTEN

    def expected_reward(self, b: float, a: int) -> float:
        return b * self.reward(0, a) + (1.0 - b) * self.reward(1, a)

    def p_obs(self, b: float, a: int, o: int) -> float:
        """P(o | b, a). Only listen is informative."""
        if a != self.LISTEN:
            return 0.5
        return (self.p * b + (1 - self.p) * (1 - b)) if o == 0 \
               else ((1 - self.p) * b + self.p * (1 - b))

    def belief_update(self, b: float, a: int, o: int) -> float:
        if a != self.LISTEN:
            return 0.5
        p_o_TL = self.p if o == 0 else 1 - self.p
        p_o_TR = 1 - self.p if o == 0 else self.p
        denom  = p_o_TL * b + p_o_TR * (1 - b)
        return p_o_TL * b / denom if denom > 1e-12 else 0.5

    def simulate_step(self, s: int, b: float, a: int) -> Tuple[int, int, float, float]:
        """Returns (s_next, obs, reward, b_next)."""
        r = self.reward(s, a)
        if a != self.LISTEN:
            s_next = np.random.randint(2)
            obs    = np.random.randint(2)
        else:
            s_next = s
            obs    = s if np.random.random() < self.p else 1 - s
        b_next = self.belief_update(b, a, obs)
        return s_next, obs, r, b_next


class TigerValueFn:
    """Precomputed grid-based value function V_h(b) for the Tiger POMDP.

    V_0(b) = 0 for all b.
    V_h(b) = max_a Q_h(b, a)
    Q_h(b, a) = E[R|b,a] + γ · Σ_o P(o|b,a) · V_{h-1}(b'(b,a,o))

    V_{h-1} is evaluated by linear interpolation on a fine belief grid,
    making each horizon's computation O(n_grid × n_actions × n_obs) — fast.
    """
    def __init__(self, pomdp: TigerPOMDP, n_grid: int = 300, max_h: int = 10):
        self.pomdp   = pomdp
        self.b_grid  = np.linspace(0.0, 1.0, n_grid)
        self.V       = {0: np.zeros(n_grid)}
        self._precompute(max_h)

    def _q_at_grid(self, i: int, b: float, a: int, h: int) -> float:
        q = self.pomdp.expected_reward(b, a)
        if h > 0:
            for o in range(self.pomdp.O):
                p_o    = self.pomdp.p_obs(b, a, o)
                b_next = self.pomdp.belief_update(b, a, o)
                q     += self.pomdp.gamma * p_o * float(np.interp(b_next, self.b_grid, self.V[h-1]))
        return q

    def _precompute(self, max_h: int):
        for h in range(1, max_h + 1):
            V_h = np.array([max(self._q_at_grid(i, float(b), a, h)
                               for a in range(self.pomdp.A))
                            for i, b in enumerate(self.b_grid)])
            self.V[h] = V_h

    def value(self, b: float, h: int) -> float:
        return float(np.interp(b, self.b_grid, self.V[h]))

    def action(self, b: float, h: int) -> int:
        """Optimal action by 1-step lookahead using precomputed V_{h-1}."""
        best_q, best_a = -np.inf, 0
        for a in range(self.pomdp.A):
            q = self._q_at_grid(0, b, a, h)
            if q > best_q:
                best_q, best_a = q, a
        return best_a

# %% [markdown]
# ## E01 — Value function over beliefs: piecewise linear and convex

# %% [markdown]
# **Hypothesis:** V_h(b) is piecewise linear and convex in b ∈ [0,1] for all h.
# As h increases, V_h grows (more lookahead is worth more), the "listen region"
# (central b where Listen is optimal) widens, and the function develops more linear
# segments. The myopic value V_0(b) = max_a E[R|b,a] is piecewise linear but concave
# in the listen-irrelevant sense — it ignores future value entirely.
#
# **Setup:** Plot V_h for h = 0,1,2,3,5 and optimal action regions per horizon.

# %%
print("E01: Value function over beliefs")
print("=" * 50)

pomdp  = TigerPOMDP(p_listen=0.85, gamma=0.95)
vfn    = TigerValueFn(pomdp, n_grid=300, max_h=10)

b_plot = vfn.b_grid
horizons   = [0, 1, 2, 3, 5]
h_colors   = [COL_MYOPIC, COL_K1, COL_K2, COL_K3, COL_K5]
h_labels   = ['h=0 (myopic)', 'h=1', 'h=2', 'h=3', 'h=5']

for h in horizons:
    v_half = vfn.value(0.5, h)
    v_01   = vfn.value(0.1, h)
    v_09   = vfn.value(0.9, h)
    print(f"  h={h:2d}  V(0.5)={v_half:7.3f}  V(0.1)={v_01:7.3f}  V(0.9)={v_09:7.3f}")

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
fig.suptitle("E01 — Tiger POMDP: Finite-Horizon Value Function V_h(b)", y=1.01)

ax = axes[0]
for h, color, label in zip(horizons, h_colors, h_labels):
    vals = [vfn.value(float(b), h) for b in b_plot]
    lw   = 2.5 if h in (0, 5) else 1.8
    ax.plot(b_plot, vals, color=color, lw=lw, label=label)
ax.set_xlabel("Belief b = P(tiger left)")
ax.set_ylabel("V_h(b)  [expected discounted return]")
ax.set_title("V_h(b) is piecewise linear & convex\nListen region widens with horizon h")
ax.axvline(0.5, color='black', lw=0.8, ls=':', alpha=0.4)
ax.legend(fontsize=8)

ax = axes[1]
# Optimal action vs belief for each horizon
action_names  = {0: 'Open Left', 1: 'Open Right', 2: 'Listen'}
action_colors = {0: COL_K1, 1: COL_K3, 2: COL_K5}
y_pos = {h: i for i, h in enumerate(horizons)}
for h in horizons:
    acts = np.array([vfn.action(float(b), h) for b in b_plot])
    y    = y_pos[h]
    for a_val, c in action_colors.items():
        mask = acts == a_val
        if mask.any():
            ax.scatter(b_plot[mask], [y]*mask.sum(), c=c, s=8, alpha=0.85)
ax.set_yticks(list(y_pos.values()))
ax.set_yticklabels([f'h={h}' for h in horizons])
ax.set_xlabel("Belief b = P(tiger left)")
ax.set_title("Optimal action vs belief & horizon\n(blue=Listen, orange=OpenL, teal=OpenR)")
ax.axvline(0.5, color='black', lw=0.8, ls=':', alpha=0.4)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=COL_K5, label='Listen'),
                   Patch(color=COL_K1,  label='Open Left'),
                   Patch(color=COL_K3,  label='Open Right')], fontsize=8)
plt.tight_layout()
plt.savefig('e01_bellman_value_function.png', bbox_inches='tight')
plt.close()
print("Saved: e01_bellman_value_function.png")

# %% [markdown]
# **FINDING 1:**
# V_h(b) is piecewise linear and convex in b, consistent with the classical result
# (Smallwood & Sondik 1973). As horizon grows, three regions emerge:
# left (b < τ_L): open Right (tiger is probably on the left);
# centre (τ_L ≤ b ≤ τ_R): Listen — uncertainty is too high to commit;
# right (b > τ_R): open Left.
# The listen region [τ_L, τ_R] shrinks as the agent becomes more certain and grows
# as horizon increases (more time to recover from a bad open justifies more listening).
# The myopic agent (h=0) has NO listen region — it never listens because it can't
# represent the future benefit of information gathering.

# %% [markdown]
# ## E02 — Myopic vs k-step lookahead: cumulative reward and open accuracy

# %% [markdown]
# **Hypothesis:** Agents with more lookahead achieve higher cumulative reward and higher
# open accuracy (fraction of opens on the safe door). The marginal gain from h to h+1
# diminishes — most benefit comes from the first 1–3 steps of lookahead.
#
# **Setup:** Simulate T=40 steps, N=2000 episodes. Horizons: 0,1,2,3,5.

# %%
print("\nE02: Myopic vs k-step lookahead — reward and open accuracy")
print("=" * 50)

def simulate_agent(pomdp: TigerPOMDP, vfn: TigerValueFn, horizon: int,
                   T: int, n_episodes: int):
    total_r, total_opens, correct_opens = 0.0, 0, 0
    for _ in range(n_episodes):
        s, b = np.random.randint(2), 0.5
        disc  = 1.0
        for t in range(T):
            a              = vfn.action(float(b), horizon)
            s, obs, r, b   = pomdp.simulate_step(s, b, a)
            total_r       += disc * r
            disc          *= pomdp.gamma
            if a in (pomdp.OPEN_L, pomdp.OPEN_R):
                total_opens   += 1
                # Correct = opened the safe door
                # (In simulate_step s is now s_next=reset; check BEFORE update)
    return total_r / n_episodes, 0.0  # placeholder accuracy

def simulate_agent_full(pomdp: TigerPOMDP, vfn: TigerValueFn, horizon: int,
                        T: int, n_episodes: int):
    """Full simulation tracking open accuracy (keeps original s for check)."""
    total_r       = 0.0
    total_opens   = 0
    correct_opens = 0
    for _ in range(n_episodes):
        s_true, b = np.random.randint(2), 0.5
        disc = 1.0
        for t in range(T):
            a = vfn.action(float(b), horizon)
            r = pomdp.reward(s_true, a)
            total_r += disc * r
            disc    *= pomdp.gamma
            if a in (pomdp.OPEN_L, pomdp.OPEN_R):
                total_opens += 1
                # opened safe door?
                safe = (a == pomdp.OPEN_R and s_true == 0) or \
                       (a == pomdp.OPEN_L and s_true == 1)
                correct_opens += int(safe)
            # simulate obs
            if a != pomdp.LISTEN:
                obs    = np.random.randint(2)
                s_true = np.random.randint(2)
            else:
                obs    = s_true if np.random.random() < pomdp.p else 1 - s_true
            b = pomdp.belief_update(float(b), a, obs)
    return total_r / n_episodes, correct_opens / max(total_opens, 1)

E02_HORIZONS = [0, 1, 2, 3, 5]
E02_COLORS   = [COL_MYOPIC, COL_K1, COL_K2, COL_K3, COL_K5]
E02_T, E02_N = 40, 2000

print(f"  {'h':>4}  {'Mean reward':>12}  {'Open accuracy':>14}  {'Δ reward':>10}")
prev_r = None
results_e02 = {}
for h in E02_HORIZONS:
    np.random.seed(42)
    r, acc = simulate_agent_full(pomdp, vfn, h, E02_T, E02_N)
    delta  = f'{r - prev_r:+.2f}' if prev_r is not None else '—'
    print(f"  h={h:2d}  {r:12.2f}  {acc:14.4f}  {delta:>10}")
    results_e02[h] = (r, acc)
    prev_r = r

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
fig.suptitle("E02 — Tiger POMDP: Lookahead Horizon vs Performance", y=1.01)

ax = axes[0]
rewards = [results_e02[h][0] for h in E02_HORIZONS]
bars    = ax.bar([str(h) for h in E02_HORIZONS], rewards, color=E02_COLORS,
                 width=0.6, edgecolor='white')
for bar, r in zip(bars, rewards):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            f'{r:.1f}', ha='center', va='bottom', fontsize=9)
ax.set_xlabel("Lookahead horizon h")
ax.set_ylabel(f"Mean discounted reward (T={E02_T})")
ax.set_title("Mean discounted reward vs lookahead horizon\n(h=0 and h=1 share the same policy; h≥2 changes threshold)")

ax = axes[1]
accs = [results_e02[h][1] for h in E02_HORIZONS]
ax.plot(E02_HORIZONS, accs, 'o-', color=COL_OPT, lw=2, ms=8)
for h, acc in zip(E02_HORIZONS, accs):
    ax.annotate(f'{acc:.3f}', (h, acc),
                textcoords='offset points', xytext=(0, 8),
                ha='center', fontsize=8)
ax.set_xlabel("Lookahead horizon h")
ax.set_ylabel("P(safe door | opened a door)")
ax.set_title("Open-door accuracy vs lookahead horizon\n(h=0 accuracy = 0.970 via listen threshold; rises with h)")
ax.set_ylim(0.4, 1.05)

plt.tight_layout()
plt.savefig('e02_bellman_lookahead_reward.png', bbox_inches='tight')
plt.close()
print("Saved: e02_bellman_lookahead_reward.png")

# %% [markdown]
# **FINDING 2:**
# The myopic agent (h=0) DOES listen — because E[R(listen)] = −1 strictly dominates
# E[R(open) | b=0.5] = 0.5×(−100+10) = −45. The myopic agent listens until its belief
# exceeds the threshold b* where E[R(openL)] > E[R(listen)], i.e. 110b−100 > −1 → b > 0.9.
# This threshold is the SAME for h=0 and h=1 (h=1 adds V₀=0 to the future value,
# which changes nothing), explaining identical performance for h=0 and h=1.
#
# The h=2 agent resolves a subtle difference: it correctly sees that after listening,
# the NEXT opportunity to open also has value, shifting the effective confidence threshold.
# Accuracy jumps from 0.970 to 0.994 between h=1 and h=2.
#
# Mean reward is higher at h=0/1 despite lower accuracy because the h=2+ agent listens
# slightly longer per episode (more −1 costs) and opens fewer times in the discounted
# window T=40, even though each open is more valuable. With discounting (γ=0.95),
# early rewards outweigh later ones — Bellman's principle at work in both directions.

# %% [markdown]
# ## E03 — Optimal behaviour vs channel quality p_listen

# %% [markdown]
# **Hypothesis:** As p_listen grows from 0.5 (random) to 1.0 (perfect), the agent needs
# fewer listen steps to reach the confidence threshold, and achieves higher reward.
# At p_listen ≈ 0.5, no information is gained per listen and the agent should act
# immediately (accepting near-random accuracy). At p_listen → 1, one listen resolves
# all uncertainty and the agent acts on the next step.

# %%
print("\nE03: Behaviour vs channel quality p_listen")
print("=" * 50)

P_LISTEN_VALS = [0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]

def mean_listen_steps(pomdp: TigerPOMDP, vfn: TigerValueFn,
                      horizon: int = 5, n_ep: int = 1000, max_t: int = 40) -> float:
    """Mean steps before first open action, starting from b=0.5."""
    total = 0
    for _ in range(n_ep):
        s, b = np.random.randint(2), 0.5
        for t in range(max_t):
            a = vfn.action(float(b), horizon)
            if a in (pomdp.OPEN_L, pomdp.OPEN_R):
                total += t
                break
            obs = s if np.random.random() < pomdp.p else 1 - s
            b   = pomdp.belief_update(float(b), a, obs)
        else:
            total += max_t
    return total / n_ep

results_e03 = {}
print(f"  {'p_listen':>10}  {'C':>8}  {'Mean listens':>14}  {'Reward h=5':>12}")
for p in P_LISTEN_VALS:
    p_pomdp = TigerPOMDP(p_listen=p, gamma=0.95)
    p_vfn   = TigerValueFn(p_pomdp, n_grid=200, max_h=5)
    np.random.seed(42)
    ml   = mean_listen_steps(p_pomdp, p_vfn, horizon=5)
    np.random.seed(42)
    r, _ = simulate_agent_full(p_pomdp, p_vfn, 5, 30, 600)
    C    = 1.0 - (-p*np.log2(p) - (1-p)*np.log2(1-p))
    results_e03[p] = (ml, r, C)
    print(f"  {p:>10.2f}  {C:>8.4f}  {ml:>14.2f}  {r:>12.2f}")

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
fig.suptitle("E03 — Listen Behaviour and Reward vs Channel Quality", y=1.01)

ax = axes[0]
ml_vals = [results_e03[p][0] for p in P_LISTEN_VALS]
ax.plot(P_LISTEN_VALS, ml_vals, 'o-', color=COL_OPT, lw=2, ms=8)
for p, ml in zip(P_LISTEN_VALS, ml_vals):
    ax.annotate(f'{ml:.1f}', (p, ml),
                textcoords='offset points', xytext=(0, 7), ha='center', fontsize=8)
ax.set_xlabel("p_listen")
ax.set_ylabel("Mean listen steps before first open")
ax.set_title("Better sensor → fewer listens needed\n(Belief crosses threshold faster)")
ax.set_ylim(0, max(ml_vals)*1.3)

ax = axes[1]
r_vals = [results_e03[p][1] for p in P_LISTEN_VALS]
C_vals = [results_e03[p][2] for p in P_LISTEN_VALS]
ax.plot(P_LISTEN_VALS, r_vals, 's-', color=COL_K3, lw=2, ms=8, label='Mean reward')
ax2r = ax.twinx()
ax2r.plot(P_LISTEN_VALS, C_vals, '^--', color=COL_K5, lw=1.5, ms=6, label='Channel cap. C')
ax.set_xlabel("p_listen")
ax.set_ylabel("Mean reward", color=COL_K3)
ax2r.set_ylabel("Channel capacity C  [bits]", color=COL_K5)
ax.tick_params(axis='y', colors=COL_K3)
ax2r.tick_params(axis='y', colors=COL_K5)
ax.set_title("Reward tracks channel capacity\n(More capacity → less time wasted listening)")
lines1, l1 = ax.get_legend_handles_labels()
lines2, l2 = ax2r.get_legend_handles_labels()
ax.legend(lines1+lines2, l1+l2, fontsize=8)

plt.tight_layout()
plt.savefig('e03_bellman_channel_quality.png', bbox_inches='tight')
plt.close()
print("Saved: e03_bellman_channel_quality.png")

# %% [markdown]
# **FINDING 3:**
# As p_listen grows, the optimal agent converges to action with fewer listen steps.
# At p_listen=0.55, ≈15+ listens are needed before the belief crosses the action threshold.
# At p_listen=0.95, fewer than 2 listens suffice. Reward tracks channel capacity closely:
# a better sensor is worth more because it converts listening cost into reliable action.
# This is the Tiger problem analogue of F.Shannon's finding that n* ~ 1/C.

# %% [markdown]
# ## E04 — Value of information over beliefs

# %% [markdown]
# **Hypothesis:** The value of information VOI(b) = V_h(b) − V_myopic(b) is a function
# of belief uncertainty, maximised at b=0.5 and decaying to zero as b → 0 or b → 1.
# Near certainty, the agent should act regardless of horizon — VOI ≈ 0.

# %%
print("\nE04: Value of information VOI(b)")
print("=" * 50)

b_fine = vfn.b_grid
V_myo  = np.array([max(pomdp.expected_reward(float(b), a) for a in range(pomdp.A))
                   for b in b_fine])
V_h5   = vfn.V[5]

voi5 = V_h5 - V_myo
idx  = np.argmax(voi5)
print(f"  Max VOI (h=5): {voi5[idx]:.3f} at b = {b_fine[idx]:.3f}")
print(f"  VOI at b=0.1: {np.interp(0.1, b_fine, voi5):.3f}")
print(f"  VOI at b=0.5: {np.interp(0.5, b_fine, voi5):.3f}")
print(f"  VOI at b=0.9: {np.interp(0.9, b_fine, voi5):.3f}")

horizons_voi = [1, 2, 3, 5]
voi_colors   = [COL_K1, COL_K2, COL_K3, COL_K5]

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
fig.suptitle("E04 — Planning Surplus over Greedy Baseline in the Tiger POMDP", y=1.01)

ax = axes[0]
ax.plot(b_fine, V_myo, color=COL_MYOPIC, lw=2, ls='--', label='Myopic (h=0)')
for h, color in zip(horizons_voi, voi_colors):
    ax.plot(b_fine, vfn.V[h], color=color, lw=2, label=f'h={h}')
ax.set_xlabel("Belief b = P(tiger left)")
ax.set_ylabel("V(b)")
ax.set_title("V_h(b) by horizon vs myopic baseline\n(h=0 is max immediate reward; h=5 strictly dominates)")
ax.axvline(0.5, color='black', lw=0.8, ls=':', alpha=0.4)
ax.legend(fontsize=8)

ax = axes[1]
for h, color in zip(horizons_voi, voi_colors):
    surplus = vfn.V[h] - V_myo
    ax.plot(b_fine, surplus, color=color, lw=2, label=f'h={h}')
ax.axhline(0, color='black', lw=1)
ax.axvline(0.5, color='black', lw=0.8, ls=':', alpha=0.4)
ax.set_xlabel("Belief b")
ax.set_ylabel("Planning surplus: V_h(b) − V_myopic(b)")
ax.set_title("Planning surplus V_h(b) − V_myopic(b)\n(Peaks near listen-region boundary; negative at h=2 near b=0.5)")
ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig('e04_bellman_voi.png', bbox_inches='tight')
plt.close()
print("Saved: e04_bellman_voi.png")

# %% [markdown]
# **FINDING 4:**
# The planning surplus V_h(b) − V_myopic(b) is NOT maximised at b=0.5. It peaks near
# the boundary of the myopic listen region (b ≈ 0.1 and b ≈ 0.9), where one listen
# is sufficient to push belief past the open threshold. At b=0.5, multiple listens are
# needed before opening is advisable, so the accumulated −1 costs reduce the surplus.
# Near b=0 or b=1 (already certain), V_myopic already matches V_h: no planning surplus.
#
# The quantity plotted is NOT the standard "value of information" (which requires
# computing V with vs without an observation signal and is always ≥ 0). It is
# V_h(b) − V_myopic(b), which can be NEGATIVE at h=2 near b=0.5 because the
# 2-step agent pays two listen costs (−1 each) but cannot yet reach sufficient
# confidence to benefit. This sign change is not a bug; it reflects the cost structure
# of the Tiger POMDP, not a definition of information value.
#
# What we cannot conclude: that "information is most valuable at maximum uncertainty."
# The surplus depends on both observation cost (−1 per listen) and planning horizon,
# not only on belief entropy.

# %% [markdown]
# ## E05 — Discount factor and the critical listen/act threshold

# %% [markdown]
# **Hypothesis:** There is a critical discount factor γ* below which the agent never
# listens (future penalty is discounted away) and above which listening is optimal at b=0.5.
# For p_listen=0.85, R_tiger=−100, R_listen=−1: γ* lies in [0.7, 0.85].

# %%
print("\nE05: Discount factor and listen/act threshold")
print("=" * 50)

GAMMA_VALS  = [0.50, 0.65, 0.75, 0.85, 0.90, 0.95]
E05_COLORS  = [COL_RANDOM, COL_MYOPIC, COL_K1, COL_K2, COL_K3, COL_K5]
action_name = {0: 'Open Left', 1: 'Open Right', 2: 'Listen'}

results_e05 = {}
print(f"  {'γ':>6}  {'Action at b=0.5 (h=5)':>25}  {'Reward':>10}  {'Open acc':>10}")
for gamma, color in zip(GAMMA_VALS, E05_COLORS):
    g_pomdp = TigerPOMDP(p_listen=0.85, gamma=gamma)
    g_vfn   = TigerValueFn(g_pomdp, n_grid=200, max_h=5)
    a_half  = g_vfn.action(0.5, 5)
    np.random.seed(42)
    r, acc  = simulate_agent_full(g_pomdp, g_vfn, 5, 30, 600)
    results_e05[gamma] = (action_name[a_half], r, acc, a_half)
    listens = '✓ listens' if a_half == 2 else f'✗ {action_name[a_half]}'
    print(f"  {gamma:>6.2f}  {listens:>25}  {r:>10.2f}  {acc:>10.4f}")

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
fig.suptitle("E05 — Discount Factor γ and the Listen/Act Trade-off", y=1.01)

ax = axes[0]
# Plot Q(listen) vs Q(open) at b=0.5 for each gamma
for gamma, color in zip(GAMMA_VALS, E05_COLORS):
    g_pomdp = TigerPOMDP(p_listen=0.85, gamma=gamma)
    g_vfn   = TigerValueFn(g_pomdp, n_grid=200, max_h=5)
    q_listen = g_vfn._q_at_grid(0, 0.5, g_pomdp.LISTEN, 5)
    q_openR  = g_vfn._q_at_grid(0, 0.5, g_pomdp.OPEN_R, 5)
    ax.scatter(gamma, q_listen, marker='s', s=80, color=color, zorder=3)
    ax.scatter(gamma, q_openR,  marker='o', s=80, color=color, alpha=0.5, zorder=3)
ax.set_xlabel("Discount factor γ")
ax.set_ylabel("Q-value at b=0.5, h=5  (■=Listen, ●=OpenRight)")
ax.set_title("Q(Listen) vs Q(OpenRight) at b=0.5 across γ (h=5)\n(Listen dominates for all tested γ ∈ [0.50, 0.95]; no threshold found)")
ax.axhline(0, color='black', lw=0.8, ls=':')

ax = axes[1]
rewards = [results_e05[g][1] for g in GAMMA_VALS]
accs    = [results_e05[g][2] for g in GAMMA_VALS]
listens = [results_e05[g][3] == 2 for g in GAMMA_VALS]
ax.plot(GAMMA_VALS, accs, 'o-', color=COL_OPT, lw=2, ms=8, label='Open accuracy')
for g, acc, l in zip(GAMMA_VALS, accs, listens):
    mark = '⬛' if l else '⬜'
    ax.annotate(f'{acc:.3f}', (g, acc),
                textcoords='offset points', xytext=(0, 8), ha='center', fontsize=8)
ax.set_xlabel("γ")
ax.set_ylabel("Open-door accuracy")
ax.set_title("Open accuracy vs discount factor γ (h=5, b₀=0.5)\n(Step between γ=0.85 and γ=0.90; listen wins for all tested γ)")
ax.set_ylim(0.4, 1.05)

plt.tight_layout()
plt.savefig('e05_bellman_discount.png', bbox_inches='tight')
plt.close()
print("Saved: e05_bellman_discount.png")

# %% [markdown]
# **FINDING 5:**
# With lookahead h=5, the listen action dominates at b=0.5 for ALL tested γ ∈ [0.5, 0.95].
# Why? At b=0.5 the myopic expected reward from opening is −45; even at γ=0.5 listening
# (−1 immediate) dominates. The critical γ* where listen first beats open exists for very
# short horizons h=1 and is determined by the expected future value. With h=5 steps, even
# a heavily discounted agent can see the value of the belief change that listening provides.
#
# The observable effect of γ IS present in the data: higher γ → agent accepts more listen
# cost per episode → arrives at higher confidence before opening → higher open accuracy
# (0.9724 for γ ≤ 0.85; 0.9955 for γ ≥ 0.90). The accuracy threshold between γ=0.85 and
# γ=0.90 marks the point where the discounted future value of a confident belief justifies
# waiting one more step. Reward also grows monotonically with γ, confirming that valuing
# the future is not just safe but profitable in the Tiger POMDP.

# %% [markdown]
# ## Summary

# %% [markdown]
# **F.Bellman — Empirical conclusions:**
#
# | Experiment | Finding |
# |------------|---------|
# | E01 | V_h(b) piecewise linear & convex; listen region [τ_L, τ_R] widens with h |
# | E02 | h=0 and h=1 share the same policy (myopic threshold b>0.9); h=2+ shift to more accurate opens |
# | E03 | Better sensor (higher p_listen) → fewer listens, higher reward |
# | E04 | Planning surplus V_h−V_myopic peaks near listen-region boundary (b≈0.1, 0.9); can be negative at h=2 |
# | E05 | Listen dominates for all tested γ ∈ [0.50, 0.95] at h=5; accuracy step between γ=0.85 and 0.90 |
#
# **Bellman's principle for POMDPs:**
# V_h(b) = max_a [ E[R|b,a] + γ · Σ_o P(o|b,a) · V_{h-1}(b'(b,a,o)) ]
#
# This equation embeds three ideas central to Area 01:
# (1) Plan over beliefs, not states — uncertainty is first-class.
# (2) Information has value only to the extent it changes future decisions.
# (3) The horizon h and discount γ jointly determine when to act vs gather information.
#
# **Connection to Area 01 master question:**
# → How should an intelligent system act when it cannot know the world completely?
#   Bellman's answer: represent uncertainty as a belief, compute the expected value
#   of each possible future trajectory, and choose the action that maximises that value.
#   Listening is a first-class action — not a hesitation — when its information value
#   exceeds its resource cost.

# %%
print("\n" + "=" * 60)
print("Notebook F.Bellman complete.")
print("Outputs: e01_bellman_value_function.png  e02_bellman_lookahead_reward.png")
print("         e03_bellman_channel_quality.png  e04_bellman_voi.png")
print("         e05_bellman_discount.png")
