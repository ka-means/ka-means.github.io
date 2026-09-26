---
layout: page
title: "Research Portfolio"
description: A structured research system on autonomous intelligent systems, organized around 20 research areas, master questions, hypotheses, experiments, and their connections to each other.
importance: 1
category: AOOS
tags: research
related_publications: false
---

This portfolio is not a collection of independent demos. It is a structured research system for the study of autonomous intelligent systems, organized around research areas, master questions, derived questions, hypotheses, experiments, methods, cross disciplinary inspiration, testbeds, perturbation and stress tests, evidence, findings, failures, transfer experiments, open questions, and the connections between all of the above.

Every project in this portfolio preserves that architecture. Unknown information is marked explicitly as pending rather than filled in with invented results, findings, citations, or conclusions.

## The Fundamental Question

Every project in this portfolio ultimately contributes, in some small and explicit way, to one question:

**What does it actually take for a system to become autonomous?**

The current portfolio thesis is:

How can autonomous systems know, decide, act, cooperate, adapt and discover under uncertainty, limited resources and changing conditions, while remaining controllable, interpretable, safe and resilient?

No single project is expected to answer this thesis in full. Each project addresses a small, explicit part of it, and the connections between projects are where the larger picture accumulates.

## Portfolio Architecture

Each project carries a permanent identifier in the form `AREA.PROJECT` (for example `03.1`), a lifecycle status, and a research maturity level that can advance independently of status. Full definitions of the identifier scheme, lifecycle stages, maturity levels, and the required project structure are maintained as internal working conventions for this portfolio and are applied consistently as projects are created.

## The 20 Research Areas

<div class="table-responsive">
<table class="table">
<thead>
<tr>
<th>Area</th>
<th>Master question</th>
</tr>
</thead>
<tbody>
<tr><td><a href="{{ '/projects/01/' | relative_url }}">01 Decision-Making Under Uncertainty</a></td><td>How should an intelligent system act when it cannot know the world completely?</td></tr>
<tr><td><a href="{{ '/projects/02/' | relative_url }}">02 Interactive Reinforcement Learning</a></td><td>How should an intelligent system learn from another intelligence?</td></tr>
<tr><td><a href="{{ '/projects/03/' | relative_url }}">03 Controllable Autonomy &amp; Agency</a></td><td>When should an intelligent system act by itself, and when should it surrender agency?</td></tr>
<tr><td><a href="{{ '/projects/04/' | relative_url }}">04 Explainable Reinforcement Learning</a></td><td>What does it mean for an intelligent system to understand and explain its own decisions?</td></tr>
<tr><td><a href="{{ '/projects/05/' | relative_url }}">05 Hierarchical RL &amp; Skill Learning</a></td><td>How can complex behaviour emerge from reusable skills?</td></tr>
<tr><td><a href="{{ '/projects/06/' | relative_url }}">06 Embodied Robot Learning</a></td><td>How does having a body change intelligence?</td></tr>
<tr><td><a href="{{ '/projects/07/' | relative_url }}">07 Multi-Agent Reinforcement Learning</a></td><td>What changes when intelligence is no longer alone?</td></tr>
<tr><td><a href="{{ '/projects/08/' | relative_url }}">08 Emergent Coordination &amp; Collective Intelligence</a></td><td>How can global order emerge without anyone designing it?</td></tr>
<tr><td><a href="{{ '/projects/09/' | relative_url }}">09 Multi-Agent Communication</a></td><td>What information must intelligences exchange in order to cooperate?</td></tr>
<tr><td><a href="{{ '/projects/10/' | relative_url }}">10 Distributed Agency</a></td><td>Where does agency reside when many intelligences control one system?</td></tr>
<tr><td><a href="{{ '/projects/11/' | relative_url }}">11 UAV &amp; Mobile Robot Autonomy</a></td><td>What does it take for an intelligent agent to operate independently in an open world?</td></tr>
<tr><td><a href="{{ '/projects/12/' | relative_url }}">12 Space &amp; Satellite Autonomous Agents</a></td><td>How should intelligence behave when observation, computation, communication and intervention are scarce?</td></tr>
<tr><td><a href="{{ '/projects/13/' | relative_url }}">13 Multimodal Robot Learning</a></td><td>How should an intelligent system construct one reality from multiple imperfect views of the world?</td></tr>
<tr><td><a href="{{ '/projects/14/' | relative_url }}">14 Adaptive Multi-Source Learning</a></td><td>How should an intelligent system decide whom and what to trust?</td></tr>
<tr><td><a href="{{ '/projects/15/' | relative_url }}">15 Continual Learning &amp; Online Adaptation</a></td><td>How can an intelligent system change without forgetting what made it capable?</td></tr>
<tr><td><a href="{{ '/projects/16/' | relative_url }}">16 Failure, Recovery &amp; Resilience</a></td><td>What does it mean for an intelligent system to survive failure?</td></tr>
<tr><td><a href="{{ '/projects/17/' | relative_url }}">17 Agentic AI &amp; Robotics</a></td><td>How can goals become autonomous sequences of meaningful action?</td></tr>
<tr><td><a href="{{ '/projects/18/' | relative_url }}">18 Transfer Learning &amp; Sim-to-Real</a></td><td>What knowledge remains true when the world changes?</td></tr>
<tr><td><a href="{{ '/projects/19/' | relative_url }}">19 Safe &amp; Constrained Reinforcement Learning</a></td><td>How should an intelligent system pursue goals when some actions must never be acceptable?</td></tr>
<tr><td><a href="{{ '/projects/20/' | relative_url }}">20 Scientific Autonomy</a></td><td>Can an intelligent system decide what it needs to discover next?</td></tr>
</tbody>
</table>
</div>

## Portfolio Status

{% assign all_projects = site.research_projects %}

{% if all_projects.size > 0 %}

<ul class="post-list">
{% for project in all_projects %}
  <li>
    <h3><a class="post-title" href="{{ project.url | relative_url }}">{{ project.id }} {{ project.title }}</a></h3>
    <p>{{ project.research_question }}</p>
  </li>
{% endfor %}
</ul>

{% else %}

No individual research projects have been created yet. This page and the 20 area pages it links to are the initial structure the portfolio will grow from.

{% endif %}

## Guiding Questions

Across all 20 areas, this portfolio keeps returning to the same underlying set of questions:

- What can the system know?
- What does it not know?
- How does it learn?
- How does it decide?
- When should it act?
- When should it ask?
- Who should have authority?
- How does it interact with other intelligences?
- What does it communicate?
- What does it trust?
- What happens when the world changes?
- What happens when the system changes?
- What happens when something fails?
- What knowledge transfers?
- What actions should remain forbidden?
- What should the system investigate next?

## What This Portfolio Optimizes For

This portfolio is not optimized for the appearance of completeness. It is optimized for traceability, reproducibility, intellectual coherence, experimental clarity, honest uncertainty, connection between questions, and cumulative knowledge. A project with one well designed experiment and several important open questions is treated as more valuable than many disconnected demonstrations.
