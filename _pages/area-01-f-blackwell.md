---
layout: page
title: "F.Blackwell: Is a More Informative Observation Always Better?"
description: Foundation experiment for Area 01, Decision-Making Under Uncertainty, testing the Blackwell sufficiency theorem and whether information gain always translates into decision value.
permalink: /projects/01/f/blackwell/
related_publications: false
---

**Area:** [01 Decision-Making Under Uncertainty](/projects/01/)
**Series:** F, Foundation Experiments
**Identifier:** F.Blackwell
**Founding Thesis:** A Blackwell-superior observation structure is always at least as good as a Blackwell-inferior one, for any decision problem, any prior, and any agent that uses the observation optimally.

This notebook tests the Blackwell sufficiency theorem with a Bayesian agent across five conditions: confirming the Blackwell ordering itself, verifying the garbling construction that turns a more informative structure into a less informative one, showing that information gain can leave decision value unchanged when the reward structure makes it irrelevant, showing that a strong prior collapses the value of new observations, and testing whether combining two independent sensors is used optimally.

The notebook defines the environment, agents and experiments but has not yet been executed. No results are reported here yet. Running it and recording the findings is still pending, consistent with the F-series status on the [Area 01 page](/projects/01/).

<div class="d-flex">
  <a href="{{ '/assets/notebooks/f-blackwell.py' | relative_url }}" class="btn btn-outline-primary" download>Download Script (.py)</a>
</div>

{::nomarkdown}
{% jupyter_notebook "/assets/notebooks/f-blackwell.ipynb" %}
{:/nomarkdown}
