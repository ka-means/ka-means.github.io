---
layout: page
title: "Real Autonomy in Mining: Four Experiments to Understand What Happens Beyond the Autonomous Truck"
description: A vehicle may operate without a driver and still belong to a fragile, poorly coordinated system that depends on human decisions. This project uses a digital twin to study four less visible dimensions of mining autonomy — model validity, information latency, interoperability, and the distribution of control among people, centralised systems, and decentralised agents.
importance: 1
category: AOOS
tags: engineering
related_publications: false
---

When we talk about autonomous haulage in mining, we usually think first about the truck: its sensors, perception, navigation, and ability to travel without a driver. Yet a mine does not produce simply because one vehicle can move autonomously. It produces because an entire fleet can coordinate with shovels, dump points, crushers, roads, dispatch systems, operators, and other equipment.

That shift in scale changes the question. It is not enough to ask whether the truck is autonomous. We must also ask:

- Is the information used to make decisions current?
- Does the system remember the decisions it has just made?
- Can it coordinate with equipment from other manufacturers and with manually operated vehicles?
- What happens when the central system fails?
- Where should the human sit: approving every decision, supervising the system, or managing exceptions?
- Could a decentralised layer sustain the operation when the central architecture loses visibility?

To explore these questions, we developed a series of four computational notebooks under the title _Real Autonomy in Autonomous Haulage_. The notebooks share the same simulator, but each examines a different dimension of the problem. The aim is not to declare a winning technology. It is to build a transparent environment in which we can formulate hypotheses, observe mechanisms, and identify the evidence that is still missing.

**Notebooks in this project:**

- [Notebook 0 — Calibration and TUM Accounting](/vault/colab/calibration-and-tum-accounting/)
- [Notebook 1 — RL Dispatch Under Information Latency](/vault/colab/rl-dispatch-information-latency/)
- [Notebook 2 — Heterogeneous Autonomous Communication](/vault/colab/heterogeneous-autonomous-communication/)
- [Notebook 3 — Human-in-the-Loop vs. Autonomous vs. Stigmergic-Inspired Heuristic](/vault/colab/human-in-the-loop-vs-autonomous-vs-stigmergic-control/)

## A Small but Deliberately Transparent Digital Twin

The project represents the haulage operation of an open-pit copper mine, anonymised as Mine A. The baseline configuration includes 23 autonomous haul trucks, five shovels, and one dump point with two bays. Each simulated shift lasts 12 hours, with the first hour discarded as a warm-up period.

The model reproduces ten operating phases: travelling empty, queuing and spotting at the source, waiting and loading, travelling full, queuing and spotting at the destination, waiting, and dumping. Every minute of every truck is also assigned to a Time Usage Model (TUM) category: production, waiting, queuing, process delay, autonomy event, maintenance, or waiting for dispatch.

The main indicators are:

- fleet production in tonnes per hour;
- cycle time;
- source and destination queues;
- availability and utilisation;
- shovel hang time;
- interaction stops and emergency stops;
- time spent waiting for decisions or approvals.

Durations are not constant. They are sampled from lognormal distributions, and the model includes failures, repairs, refuelling, dump-point blockages, and process delays. Each scenario is replicated using different seeds, and 95% confidence intervals are calculated using Student's t distribution.

This matters because a single simulation run can be misleading. One policy may appear better simply because fewer failures occurred during that shift. Replication allows us to ask whether a difference persists under simulated variability.

It is equally important to define what this model is not. It is not a complete operational replica of Mine A. It does not represent ore grades, blending constraints, bench sequences, detailed road geometry, weather, or a production plan. Some parameters come from aggregated dashboard indicators; others were calibrated, while others remain engineering assumptions. The results are therefore comparisons conditional on the model — not forecasts for a real mine.

With that boundary made explicit, the four notebooks can be read as four stages of one investigation.

## Notebook 0: Is the Twin Coherent Enough for Experimentation? {#notebook-0}

_[Run the interactive notebook →](/vault/colab/calibration-and-tum-accounting/)_

### The Question

Before comparing algorithms, we must establish whether the simulator can reproduce the broad form of the haul cycle and the observed time accounting. The first question was:

Can a compact model reproduce the operation's aggregated indicators with enough coherence to support policy comparisons within the same twin?

This question may sound less exciting than training a reinforcement-learning agent, but it is the most important one. A sophisticated algorithm does not repair a misspecified environment; it merely learns how to exploit its errors.

### What We Did

We compared the baseline allocation plan with values extracted from the operational dashboard: phase times, availability, utilisation, queues, productivity, and shovel hang time. We also classified every apparent agreement according to its origin:

- input, when the value was taken directly from the dashboard;
- by construction, when it followed directly from selected parameters;
- calibration target, when the model was adjusted to approximate it;
- check, when the indicator was not used in calibration.

This distinction avoids a common mistake: presenting as validation something that the model received as an input.

### The Provisional Answer

The simulated total cycle was 32.24 minutes, compared with 33.51 minutes in the dashboard. Source queue was 5.81 minutes, compared with 6.06; destination queue was 1.54 versus 1.56 minutes; and utilisation was 67.31% versus 66.20%.

In other words, the model can approximate the aggregated indicators it was designed to reproduce. But much of that agreement is calibration.

The most informative test was the one that failed. Simulated shovel hang time reached 4.41 minutes, almost twice the dashboard value of 2.24 minutes. This discrepancy suggested that the five-shovel structure and the 9-5-4-3-2 baseline allocation might be generating a congestion pattern different from the one observed at the mine.

We therefore tested five alternative structures. In every case, a greedy dispatcher using current information outperformed the baseline plan, but the size of the improvement ranged from 5.5% to 16.7%. With four reliable shovels and a more balanced allocation, shovel hang time fell to 2.2 minutes — very close to the dashboard. Yet that same variant did not simultaneously reproduce the observed queue and utilisation.

The most honest conclusion from Notebook 0 is therefore twofold:

1. The twin is internally coherent and useful for comparing policies under common assumptions.
2. The magnitude of the gains depends strongly on how the operating structure is represented.

As a benchmark, greedy dispatch with a current snapshot of committed trucks and shovel status increased throughput from 10,751 to 11,924 t/h — an improvement of 1,173 t/h, or 10.9%. Source queue fell from 5.81 to 2.00 minutes.

We do not describe this result as an "upper bound." The algorithm does not observe the entire physical state, and the model allows the shovel and haul mix to change freely. It is simply a reference point for the value of improved allocation within the assumed structure.

### The Questions It Opens

- How many shovels were genuinely active during the reference period?
- What was the effective truck allocation by shovel?
- How much of the source queue came from dispatch, and how much from failures, geometry, or production-plan constraints?
- Would the comparison change if grade, blending, and production priorities were included?
- Do the conclusions survive in a period of data not used for calibration?

The natural next step is not more algorithmic complexity. It is structural validation using Fleet Management System (FMS) events and a period held out from calibration. Since no such data is available for this project, the notebook also includes a synthetic, event-level log built from the simulator itself, used only to demonstrate what a calibration-versus-holdout validation would look like methodologically. Reconstructed cycle time and throughput track the model's own internal figures within a few percent, but reconstructed queue durations diverge sharply from the dashboard-calibrated ones, because the two are different statistics: a per-occurrence mean computed from logged events versus a per-trip mean that also counts trips with no queue at all. This is not a validation against Mine A. It is a reminder that an event-log pipeline can silently redefine the indicator it claims to measure.

## Notebook 1: What Does Stale Information Cost, and What Does RL Actually Add? {#notebook-1}

_[Run the interactive notebook →](/vault/colab/rl-dispatch-information-latency/)_

### The Question

A dispatch system operates as a feedback loop: it observes the operation, assigns trucks, and observes again. But if information arrives five or fifteen minutes late, the picture used for the next decision no longer describes the current state.

This led to three questions:

1. How much production is lost when dispatch trusts a stale snapshot literally?
2. Is it enough to correct that snapshot using the decisions made since it was captured?
3. Does a reinforcement-learning agent add anything beyond that simple correction?

### The Mechanism: The System Forgets Its Own Actions

Imagine that the dashboard shows few trucks committed to one shovel. The dispatcher sends a truck there, but that decision will take several minutes to appear in telemetry. Before the picture updates, other trucks finish dumping and consult the same stale snapshot. They all see the same apparently empty shovel and receive the same destination. The result is a convoy followed by a queue.

The proposed correction is simple: take the stale snapshot and add the trucks that the dispatcher itself has assigned during the latency window. The system receives no new field information. It simply stops forgetting its own decisions.

### What We Compared

We evaluated six policies under information delays of 0, 5, and 15 minutes:

- a static plan;
- nearest shovel;
- a probabilistic routing mix without queue telemetry, although it knows which shovels are available;
- a greedy rule that trusts the stale snapshot;
- the same greedy rule corrected using recent assignments;
- a linear RL agent trained for each latency level.

The agent uses 12 features and minimises the time from dispatch until loading is completed. Importantly, it does not start from a blank slate: its features include a corrected estimate constructed using a 4.5-minute service constant. The comparison is therefore not "pure learning" versus "manual engineering." It asks whether a learned linear combination improves upon an explicit rule that already contains the correction.

### The Provisional Answer

The rule that trusts stale information falls from 11,905 t/h at zero latency to 10,881 t/h with a five-minute delay and 9,514 t/h with a fifteen-minute delay. In the final scenario, source queue reaches 11.3 minutes and the policy performs worse than the static plan.

The correction recovers much of the loss:

- at five minutes it adds 983 ± 165 t/h relative to the stale rule;
- at fifteen minutes it adds 2,008 ± 191 t/h.

With fifteen minutes of delay, source queue falls from 11.3 to 1.5 minutes. The conclusion is strikingly practical: before training a more complex policy, make sure the system correctly accounts for its own pending decisions.

What about RL? The difference between the agent and the corrected rule was:

- −363 ± 277 t/h at zero latency;
- −32 ± 168 t/h at five minutes;
- +90 ± 227 t/h at fifteen minutes.

The corrected rule is better in the zero-latency scenario and statistically tied with RL in the other two. At fifteen minutes, both achieve similar throughput, but through different operating patterns: the corrected rule has 1.5 minutes of source queue and 77.3% utilisation; the agent has 3.7 minutes and 71.1%. RL concentrates more work on the nearer shovels, while the rule uses more of the distant-shovel capacity.

The notebook does not conclude that reinforcement learning "does not work." Its conclusion is more specific: this linear agent, with this training process and these features, does not demonstrate an advantage over a transparent rule that corrects latency using a memory of recent decisions.

We also observed sensitivity to distribution shift. An agent trained with instantaneous information lost 862 t/h when deployed with a fifteen-minute delay, relative to the agent trained for that condition. A learned policy should not be validated once and assumed to remain valid when the data pipeline changes.

### The Questions It Opens

- What happens under variable latency, bursts, message loss, or asynchronous sources?
- Can a more expressive agent outperform the rule without sacrificing interpretability and stability?
- How does the result change when grade, blending, and bench priorities must be respected?
- How much uncertainty comes from training? Here, only one training run was used for each latency.
- How does RL compare with mathematical optimisation or predictive dispatch?
- Should the agent be trained with domain randomisation so it can tolerate changes in real latency?

The future question is no longer "Can we use RL?" but "What incremental value does it deliver over the strongest simple and auditable benchmark?"

## Notebook 2: What Is the Value of Interoperability in a Heterogeneous Mine? {#notebook-2}

_[Run the interactive notebook →](/vault/colab/heterogeneous-autonomous-communication/)_

### The Question

An autonomous mine is rarely a perfectly homogeneous fleet. Trucks from different manufacturers operate alongside manually driven vehicles, light vehicles, support equipment, shovels, and other autonomy platforms. When these agents cannot share intent, autonomous systems tend to behave conservatively: they slow down, stop, or escalate an uncertain situation.

The question was: what changes when we move from perception without communication to partial or full interoperability?

### What We Modelled

Encounters with external agents are represented through an interaction rate during travel. Without communication, an encounter produces a hard stop and may escalate to an emergency stop. With communication, it becomes a short negotiated slowdown.

Full interoperability also includes an additional assumption: a truck–shovel handshake that reduces part of the spotting and waiting-for-load time. This point is decisive because the "full communication" scenario contains two different mechanisms: coordination on the road, and coordination between truck and shovel.

### The Provisional Answer

Mean throughput was:

- 11,333 t/h without heterogeneous communication;
- 11,881 t/h with partial coverage;
- 12,349 t/h with full interoperability.

Partial coverage added 548 ± 179 t/h (+4.8%), while full coverage added 1,016 ± 213 t/h (+9.0%) relative to no communication.

Cycle time fell from 29.4 to 28.0 minutes, and utilisation increased from 71.1% to 73.8%. Emergency stops fell from 7.8 to 4.8 and then to zero. That zero, however, must not be interpreted as a safety prediction. It is a direct consequence of the model logic: escalation can occur only after an uncoordinated encounter, and the full-coverage scenario eliminates that branch.

The TUM accounting helps explain where the improvement appears. Interaction stops fall from 2.99% to 0.49% of fleet time, while code 1010 production rises from 56.16% to 59.57%.

The aggregate queue remains almost unchanged, but the bottleneck moves. Source queue falls from 3.32 to 2.70 minutes, while destination queue rises from 1.36 to 1.65 minutes. Increasing production and releasing trucks from the source more quickly can transfer pressure to the crusher. Simply stating that "queues did not change" would conceal that movement.

The critical test was to switch off the shovel handshake. When communication improves only road interactions, the benefit falls to 372 ± 178 t/h, or 3.3%. A conditional decomposition assigns approximately 63% of the full improvement to the handshake.

That 63% is not a universal causal proportion. The two mechanisms interact: reducing loading-related time increases cycle frequency and changes congestion. Even so, the test clearly identifies the assumption most in need of real data.

Sensitivity to traffic density is equally revealing. The advantage of full interoperability over no communication grows from 4.3% under very light external traffic to around 13–14% in the densest scenarios. Interoperability appears most valuable precisely where the operation is most heterogeneous.

### The Questions It Opens

- What is the real interaction rate with external vehicles and equipment?
- How long do negotiated and uncoordinated stops actually last?
- What proportion genuinely escalates into autonomy or emergency events?
- How much can a real truck–shovel handshake reduce spotting and waiting-for-load time?
- Where are the highest-value zones: ramps, intersections, loading faces, or dump points?
- What happens under intermittent spatial coverage or a communication outage?
- Which protocols enable interoperability without introducing new cybersecurity risks?
- How should the productivity benefit be separated from the safety requirements of ISO 17757?

The notebook offers a conditional answer about productivity. Safety and certification require a different form of evidence.

## Notebook 3: Who Should Close the Control Loop? {#notebook-3}

_[Run the interactive notebook →](/vault/colab/human-in-the-loop-vs-autonomous-vs-stigmergic-control/)_

### The Question

The final notebook shifts the focus from information to governance. It compares five configurations:

1. Human-only: radio dispatch using a delayed and noisy picture.
2. Human-in-the-loop (HITL): an optimiser proposes and a person approves every assignment.
3. Human-on-the-loop (HOTL): the optimiser executes while a person supervises exceptions.
4. Central autonomy: a central optimiser with no human approval for each decision.
5. Stigmergic-inspired heuristic: decentralised coordination through environmental cost marks that evaporate over time.

An earlier version of this notebook called the fifth configuration "autopoietic," a term we have since dropped: the model does not reproduce biological autopoiesis, and "stigmergic" describes the actual mechanism without the extra metaphorical weight. Each truck contributes to shared marks based on its own local outcome; when it reaches a failed shovel and diverts, it leaves a temporary repellent mark there so other trucks avoid it until the mark decays. No truck reads a global queue vector or a central dispatch log.

We tested all five configurations during a normal shift, a 120-minute FMS outage, a 120-minute shovel failure, and a compound failure in which both events occur simultaneously.

### A Causal Precaution

These configurations do not differ along only one dimension. Information lag, noise, approval, veto behaviour, redirection delay, exception treatment, and fallback logic all change together. We therefore cannot attribute every difference to "having or not having a human." We are comparing complete governance configurations.

### The Provisional Answer Under Normal Operations

Mean throughput was:

- human-only: 10,993 t/h;
- HITL: 11,265 t/h;
- HOTL: 11,630 t/h;
- central autonomy: 11,533 t/h;
- stigmergic-inspired heuristic: 11,610 t/h.

HOTL, central autonomy, and the stigmergic-inspired heuristic are statistically indistinguishable during a normal shift. The stigmergic heuristic exceeds central autonomy by 77 ± 231 t/h, while HOTL exceeds it by 97 ± 219 t/h; both intervals include zero.

The HITL configuration performs 366 ± 205 t/h below HOTL. Part of the difference appears as approval waiting time: HITL accumulates 1.78 minutes of hold per trip. The system reduces some queueing, but replaces it with time spent waiting for a decision.

The sensitivity experiment confirms that approval latency is decisive. With an 8% veto rate, HITL produces 11,586 t/h with near-instant approval of 0.05 minutes, 11,201 with 1.5 minutes, 10,939 with 3 minutes, and 10,130 with 6 minutes. Near-zero approval is competitive with HOTL; by three minutes its mean has already fallen close to human radio dispatch.

The 8% veto does not show a consistent cost. Removing it produces differences ranging from about −79 to +107 t/h depending on latency. The evidence does not support assigning a fixed "veto cost."

### The Provisional Answer Under Failure

Under an FMS-only outage, human-only and stigmergic modes remain unchanged by construction because neither depends on the central node. With the configured fallback, the centralised modes lose less than 2%.

Under a shovel-only outage, losses are modest across all five modes. The stigmergic system must locally detect the failed shovel, mark it, and redistribute itself; that process has a cost, although a limited one in this implementation.

The difference appears during the compound failure. The stigmergic heuristic maintains 11,464 t/h, compared with 10,905 for HOTL, 10,848 for central autonomy, and 10,622 for HITL. Its advantage is:

- 559 ± 185 t/h over HOTL;
- 616 ± 147 t/h over central autonomy.

However, the result depends on the fallback selected for the centralised architectures. In the model, after waiting for several minutes, they return to a static allocation that may continue sending trucks to the failed shovel. As the fallback delay increases from 2 to 30 minutes, the advantage of the stigmergic heuristic grows. If the central modes simply hold until the FMS returns, throughput falls to around 9,000 t/h.

This does not demonstrate that decentralisation is always superior. It demonstrates something more specific: a decentralised layer may provide resilience when the alternative is a naive central fallback or prolonged waiting without local decision authority. A central fallback supported by local sensing, radio dispatch, or a distributed backup layer could reduce or eliminate the difference.

### What About Human Workload?

Human-only and HITL record approximately 366 and 373 control interventions per shift; HOTL, central autonomy, and the stigmergic heuristic each record around 4 to 4.5.

This near-zero residual does not mean an absence of human work. The model does not count every physical action performed by field crews, maintenance teams, or emergency responders. The table measures control decisions and exceptions — not total employment or operational responsibility.

### The Questions It Opens

- What would a factorial comparison look like if latency, approval, veto, and fallback were isolated?
- Which hybrid fallback best combines central coordination with safe local decision-making?
- How should fatigue, expertise, cognitive load, and loss of situation awareness be represented?
- Which events must always be escalated to a person?
- How do the results change under network partitions, GNSS loss, weather, cyberattacks, or multiple simultaneous failures?
- How should resilience be measured without reducing it to throughput?
- What is the right level of locality for the stigmergic marks: does each truck need to sense the shovel directly, or is a shared but unauthenticated mark still an honest test of decentralisation?
- How should responsibility and authority be allocated when multiple agents make local decisions?

## What Cross-Cutting Answers Does the Project Offer?

The four notebooks do not close the debate, but they support five provisional answers.

### 1. Autonomy Is a Property of the System, Not Only the Vehicle

A truck may navigate autonomously while belonging to an operation that depends on stale information, incompatible protocols, or a single central node. Operational autonomy includes coordination, information quality, recovery capability, and governance.

### 2. More Data Does Not Help if the System Forgets Its Own Decisions

Latency does more than make information old. It creates a gap between the observed state and the actions already in flight. An explicit memory of those actions can recover more value than a more complex learned controller.

### 3. The Right Benchmark Changes the Evaluation of AI

Comparing RL only with a naive rule can create an artificial advantage. In this project, the relevant benchmark is a rule that incorporates a simple physical correction. Against that benchmark, the linear agent does not demonstrate an improvement.

### 4. Interoperability Moves Bottlenecks

Reducing road stops and shovel-related delays increases production, but it may also transfer congestion towards the destination. A local improvement does not automatically produce a balanced system-wide improvement.

### 5. Decentralisation Is Valuable for the Failure It Allows the System to Survive

The stigmergic-inspired heuristic has no detectable advantage over HOTL or central autonomy during normal operation. Its value emerges when a central outage and local failure coincide, and when the central fallback is weak. The right question is not "centralised or decentralised?" but "Which capabilities must survive locally when global coordination is lost?"

## What We Still Cannot Claim

The project does not demonstrate that a real mine will obtain these exact improvements. Nor does it demonstrate that RL is unnecessary, that full communication eliminates risk, or that a stigmergic system can replace human supervision.

The results are conditioned by:

- an operation reduced to five abstract shovels and one destination;
- parameters calibrated against aggregated indicators;
- partially assumed event rates and response times;
- no grade, blending, bench sequencing, or production-plan constraints;
- a productivity representation rather than a safety model;
- a limited set of failures and policies.

This boundary does not weaken the project. It defines precisely what kind of knowledge it produces: experimental evidence within an explicit, reproducible, and contestable model.

## The Research Agenda It Opens

The next stage requires less algorithmic spectacle and more contact with the operation. The priorities are:

1. Validation using FMS events. Reconstruct trips, decisions, queues, failures, and delays at event level, and reserve an independent validation period.
2. Real mining constraints. Add grade, blending, bench priorities, routes, gradients, and destination capacity.
3. Real latency. Measure the complete distribution from sensor to decision: mean, variability, loss, asynchrony, and recovery.
4. Measurable interoperability. Estimate encounters, durations, and handshake benefits by zone and agent type.
5. Stronger comparators. Add mathematical optimisation, predictive control, and agents trained under uncertainty and domain shift.
6. Causal governance design. Separate the effects of human approval, veto, supervision, response time, and fallback.
7. Resilience and safety. Evaluate multiple scenarios and metrics beyond throughput: exposure, recovery, safe degradation, and operator workload.
8. Economic evaluation. Translate production effects into cost, required infrastructure, risk, and the option value of backup capabilities.

## An Open Conclusion

The most important lesson from these four notebooks is not a percentage. It is a change in how the problem is framed.

The initial question — "How autonomous is the truck?" — is too small. The relevant questions sit one level higher:

- What does the system know when it decides?
- What does it remember about its own actions?
- With whom can it coordinate?
- Which part of its intelligence depends on a central node?
- Which capabilities remain when that node fails?
- Where does a person add real value, and where do they merely add delay?

The simulations offer a provisional answer: robust autonomy does not emerge from progressively removing the human or from adding a more complex algorithm. It emerges from designing information, coordination, benchmarks, recovery mechanisms, and limits of authority well.

That is the space this project seeks to open: moving beyond autonomous vehicles to study autonomous systems that can operate, explain their decisions, and degrade safely when the world stops behaving as expected.

## Scope Note

This article summarises exploratory experiments conducted with a simplified digital twin and anonymised aggregated operational data. The results are not a production forecast, an operational recommendation, or a safety case. Application requires validation with held-out FMS data, mine-plan constraints, and the relevant engineering and safety standards.

## Main References

1. Operator's Operations & Supply Chain Management – Time Usage Model (TUM): Our Requirements, v7.0 (12 Jan 2023), anonymised internal standard.
2. Autonomous-Haulage Dashboard, Mine A, anonymised extracts for 9–16 March 2025.
3. Banks, J., Carson, J. S., Nelson, B. L. & Nicol, D. M. (2010). _Discrete-Event System Simulation_ (5th ed.). Pearson.
4. Law, A. M. (2015). _Simulation Modeling and Analysis_ (5th ed.). McGraw-Hill.
5. Alarie, S. & Gamache, M. (2002). Overview of solution strategies used in truck dispatching systems for open pit mines. _International Journal of Surface Mining, Reclamation and Environment_, 16(1), 59–76.
6. Sutton, R. S. & Barto, A. G. (2018). _Reinforcement Learning: An Introduction_ (2nd ed.). MIT Press.
7. ISO 17757:2019. Earth-moving machinery and mining – Autonomous and semi-autonomous machine system safety.
8. Bainbridge, L. (1983). Ironies of automation. _Automatica_, 19(6), 775–779.
9. Endsley, M. R. & Kiris, E. O. (1995). The out-of-the-loop performance problem and level of control in automation. _Human Factors_, 37(2), 381–394.
10. Bonabeau, E., Dorigo, M. & Theraulaz, G. (1999). _Swarm Intelligence: From Natural to Artificial Systems_. Oxford University Press.
