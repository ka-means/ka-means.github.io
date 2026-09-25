---
layout: page
title: "Complex Systems / Network Science"
description: Thesaurus of terms from the Complex Systems category — scale-free networks, threshold dynamics, contagion models, dissipative structures, circular causality, and spontaneous order as discovery process.
related_publications: false
permalink: /thesaurus/complex-systems-network-science/
---

**Parent article:** [Complex Systems: Order Without a Designer](/blog/2022/complex-systems-order-without-a-designer/)

---

**Scale-free network**

Network whose distribution of connections per node follows a power law: a few nodes have many connections (hubs) and most nodes have few. Described by Barabási and Albert (1999). Direct consequence for dynamics: more resilient to random failures, more vulnerable to targeted attacks on hubs. Most real-world networks, including the internet, protein interaction networks, and social networks, are approximately scale-free.

_Related:_ power law, hub, degree distribution, preferential attachment
_Cross-references:_ [Robotics / Swarm Systems](/thesaurus/robotics-swarm-systems/), [Systems Engineering](/thesaurus/systems-engineering/), [Agent-Based Modeling (ABM)](/thesaurus/agent-based-modeling/)
_Key work:_ Barabási, A. L., & Albert, R. (1999). Emergence of scaling in random networks. _Science_, 286(5439), 509–512.

**Threshold dynamics**

Behavior of systems where effects are imperceptible below a critical value and amplify discontinuously once that threshold is crossed. Fundamental characteristic of non-linear systems. Granovetter's models (1978): a behavior can remain dormant in a network and then propagate explosively when the fraction of adopters surpasses the critical threshold of enough individuals.

_Related:_ tipping point, bifurcation, cascade, phase transition
_Cross-references:_ [Agent-Based Modeling (ABM)](/thesaurus/agent-based-modeling/)
_Key work:_ Granovetter, M. (1978). Threshold models of collective behavior. _American Journal of Sociology_, 83(6), 1420–1443.

**SIR model / Contagion models**

The SIR framework (Susceptible, Infected, Recovered) is appropriate for biological contagion with immunity. Granovetter's threshold models are appropriate for social contagion where adoption depends on the fraction of neighbors who have already adopted, not on direct contact. Using them interchangeably produces incorrect predictions about propagation speed, extinction conditions, and intervention effectiveness.

_Related:_ R0, epidemic dynamics, cascade models, contagion networks
_Cross-references:_ none direct
_Key work:_ Kermack, W. O., & McKendrick, A. G. (1927). A contribution to the mathematical theory of epidemics. _Proceedings of the Royal Society A_, 115(772), 700–721.

**Dissipative structure** (Prigogine)

Ordered structure that emerges and is maintained in an open system far from thermodynamic equilibrium, through the flow and dissipation of energy to the environment. Examples: Belousov-Zhabotinsky reaction, Bénard convection, living organisms. Nobel Prize in Chemistry 1977. Functional parallel with Hayek's spontaneous order: both describe structures maintained by continuous flows, not by equilibrium states.

_Related:_ non-equilibrium thermodynamics, self-organization, entropy, emergence
_Cross-references:_ [Information Theory / Science and Technology](/thesaurus/information-theory-sci-tech/), [Praxeology / Austrian Political Economy](/thesaurus/praxeology-austrian-political-economy/)
_Key work:_ Prigogine, I., & Stengers, I. (1984). _Order Out of Chaos_. Bantam Books.

**Circular causality**

Situation where A causes B and B causes A, creating feedback loops that cannot be analyzed as linear causal chains. Structural characteristic of complex systems. The primary reason why linear models and standard regression analysis fail to predict systemic behavior: they decompose into unidirectional causalities what is fundamentally circular.

_Related:_ feedback, non-linearity, emergence, cybernetics
_Cross-references:_ [Agent-Based Modeling (ABM)](/thesaurus/agent-based-modeling/), [Systems Engineering](/thesaurus/systems-engineering/)
_Key work:_ Wiener, N. (1948). _Cybernetics_. MIT Press.

**Spontaneous order as discovery process**

In the Hayekian framework: the market is not a mechanism for allocating resources efficiently given a known set of preferences and technologies. It is a discovery process where preferences, technologies, and opportunities are revealed precisely through the competitive process. This distinction separates Austrian economics from neoclassical general equilibrium economics and has direct implications for understanding complex systems generally.

_Related:_ catallactics, market process, dispersed information, competition
_Cross-references:_ [Praxeology / Austrian Political Economy](/thesaurus/praxeology-austrian-political-economy/), [Agent-Based Modeling (ABM)](/thesaurus/agent-based-modeling/)
_Key work:_ Hayek, F. A. (1945). The use of knowledge in society. _American Economic Review_, 35(4), 519–530.

## References

Barabási, A. L., & Albert, R. (1999). Emergence of scaling in random networks. _Science_, 286(5439), 509–512.

Granovetter, M. (1978). Threshold models of collective behavior. _American Journal of Sociology_, 83(6), 1420–1443.

Hayek, F. A. (1945). The use of knowledge in society. _American Economic Review_, 35(4), 519–530.

Prigogine, I., & Stengers, I. (1984). _Order Out of Chaos: Man's New Dialogue with Nature_. Bantam Books.

Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of 'small-world' networks. _Nature_, 393, 440–442.
