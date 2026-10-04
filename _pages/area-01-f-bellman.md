---
layout: page
title: "F.Bellman: The Value of Information and Optimal Lookahead"
description: Foundation experiment for Area 01, Decision-Making Under Uncertainty, testing Bellman's principle of optimality on the Tiger Problem, where planning happens over beliefs rather than states.
permalink: /projects/01/f/bellman/
related_publications: false
---

**Area:** [01 Decision-Making Under Uncertainty](/projects/01/)
**Series:** F, Foundation Experiments
**Identifier:** F.Bellman
**Founding Thesis:** Bellman's principle of optimality (1957): a policy is optimal if and only if, at every decision point, it chooses the action that maximizes immediate reward plus the discounted value of the resulting state. In a POMDP, state is replaced by belief, a distribution over hidden states, so the agent must plan over beliefs rather than states.

This notebook tests that principle on the Tiger Problem (Cassandra, Kaelbling and Littman, 1994): two doors hide a tiger behind one and safety behind the other, and the agent can listen for a noisy clue or commit to opening a door. Five conditions are compared: the belief value function itself, myopic versus multi-step lookahead, optimal listening behavior against sensor quality, the value of information as a function of belief, and how the discount factor shifts the listen-or-act threshold.

The notebook defines the environment, agents and experiments but has not yet been executed. No results are reported here yet. Running it and recording the findings is still pending, consistent with the F-series status on the [Area 01 page](/projects/01/).

<div class="d-flex">
  <a href="{{ '/assets/notebooks/f-bellman.py' | relative_url }}" class="btn btn-outline-primary" download>Download Script (.py)</a>
</div>

{::nomarkdown}
{% jupyter_notebook "/assets/notebooks/f-bellman.ipynb" %}
{:/nomarkdown}
