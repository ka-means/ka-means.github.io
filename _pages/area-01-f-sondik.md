---
layout: page
title: "F.Sondik: Alpha-Vector Value Iteration in POMDPs"
description: Foundation experiment for Area 01, Decision-Making Under Uncertainty, testing Smallwood and Sondik's result that the POMDP value function is piecewise linear and convex, and can be represented exactly by a finite set of alpha-vectors.
permalink: /projects/01/f/sondik/
related_publications: false
---

**Area:** [01 Decision-Making Under Uncertainty](/projects/01/)
**Series:** F, Foundation Experiments
**Identifier:** F.Sondik
**Founding Thesis:** Smallwood and Sondik (1973) proved that the finite-horizon POMDP value function is piecewise linear and convex, and can be represented exactly as the upper envelope of a finite set of linear functions over the belief simplex, the alpha-vectors. This turns an uncountably infinite belief-state problem into a finite, if growing, set of linear functions, and is what makes exact POMDP planning tractable.

Where F.Bayes showed how belief updates work and F.Bellman showed that planning under uncertainty decomposes recursively, this notebook asks what the resulting value function actually looks like, and how to represent and compute it exactly. Together the two notebooks and this one establish part of the formal foundation this area works from.

The notebook defines the environment, agents and experiments but has not yet been executed. No results are reported here yet. Running it and recording the findings is still pending, consistent with the F-series status on the [Area 01 page](/projects/01/).

<div class="d-flex">
  <a href="{{ '/assets/notebooks/f-sondik.py' | relative_url }}" class="btn btn-outline-primary" download>Download Script (.py)</a>
</div>

{::nomarkdown}
{% jupyter_notebook "/assets/notebooks/f-sondik.ipynb" %}
{:/nomarkdown}
