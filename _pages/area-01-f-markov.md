---
layout: page
title: "F.Markov: Cost of Memoryless Inference Under Partial Observability"
description: Foundation experiment for Area 01, Decision-Making Under Uncertainty, measuring how much decision quality is lost when an agent acts on the latest observation alone instead of maintaining a belief over history.
permalink: /projects/01/f/markov/
related_publications: false
---

**Area:** [01 Decision-Making Under Uncertainty](/projects/01/)
**Series:** F, Foundation Experiments
**Identifier:** F.Markov
**Founding Thesis:** The Markov property holds for the belief state: the belief at time t is a sufficient statistic for the full history, which makes the belief MDP Markovian. An agent that conditions on that belief is therefore already exploiting the Markov property, not discarding it.

This notebook asks a narrower, practical question: when an agent instead acts on only its most recent observation, ignoring everything before it, how much does that memoryless approximation cost in decision quality, and at what history depth does performance recover to near-optimal? A memoryless agent, a sliding-window agent, a full belief agent and a random baseline are compared across five conditions: a baseline trajectory view, a sweep over history depth, a sweep over how fast the world changes, a joint grid of both factors, and the minimum memory depth the world's dynamics actually require.

The notebook defines the environment, agents and experiments but has not yet been executed. No results are reported here yet. Running it and recording the findings is still pending, consistent with the F-series status on the [Area 01 page](/projects/01/).

<div class="d-flex">
  <a href="{{ '/assets/notebooks/f-markov.py' | relative_url }}" class="btn btn-outline-primary" download>Download Script (.py)</a>
</div>

{::nomarkdown}
{% jupyter_notebook "/assets/notebooks/f-markov.ipynb" %}
{:/nomarkdown}
