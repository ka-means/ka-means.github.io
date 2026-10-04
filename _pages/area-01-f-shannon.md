---
layout: page
title: "F.Shannon: Channel Capacity as a Bound on Decision Quality"
description: Foundation experiment for Area 01, Decision-Making Under Uncertainty, testing whether Shannon's channel capacity theorem predicts how many observations an agent needs and how fast its uncertainty collapses.
permalink: /projects/01/f/shannon/
related_publications: false
---

**Area:** [01 Decision-Making Under Uncertainty](/projects/01/)
**Series:** F, Foundation Experiments
**Identifier:** F.Shannon
**Founding Thesis:** Shannon's channel capacity theorem: a noisy binary channel supports reliable decisions at a rate set by its capacity. That capacity should govern how many observations an agent needs and how fast its uncertainty collapses.

This notebook asks how mutual information per observation predicts decision quality, how many observations are needed to reach a target accuracy, and what happens when the agent's model of its own sensor is wrong. Five conditions are compared: the exact theoretical accuracy curve against empirical performance, cumulative log-likelihood ratio as a predictor of accuracy, the number of observations needed to reach a given accuracy as channel quality varies, how fast belief entropy decays, and what a misspecified channel model does to tracking in a world that keeps changing.

The notebook defines the environment, agents and experiments but has not yet been executed. No results are reported here yet. Running it and recording the findings is still pending, consistent with the F-series status on the [Area 01 page](/projects/01/).

<div class="d-flex">
  <a href="{{ '/assets/notebooks/f-shannon.py' | relative_url }}" class="btn btn-outline-primary" download>Download Script (.py)</a>
</div>

{::nomarkdown}
{% jupyter_notebook "/assets/notebooks/f-shannon.ipynb" %}
{:/nomarkdown}
