---
layout: page
title: "Robotics / Swarm Systems"
description: Thesaurus of terms from the Robotics category — stigmergy, network topology, spontaneous order, emergence, resilience, and distributed accountability.
related_publications: false
permalink: /thesaurus/robotics-swarm-systems/
---

**Parent article:** [Robotics: Engineering Spontaneous Order](/blog/2023/robotics-engineering-spontaneous-order/)

---

**Stigmergy**

Mechanism of indirect coordination where agents modify a shared environment and other agents respond to those modifications, without direct communication between them. Origin: entomologist Pierre-Paul Grassé (1959), studying termites. Later adopted by swarm robotics and distributed computing under the same name.

_Related:_ pheromone trails, implicit coordination, reactive agents
_Cross-references:_ [Agent-Based Modeling (ABM)](/thesaurus/agent-based-modeling/), [Systems Engineering](/thesaurus/systems-engineering/)
_Key work:_ Grassé, P. P. (1959). La théorie de la stigmergie. _Insectes Sociaux_, 6(1), 41–80.

**Network topology**

Structure defining which nodes can communicate with which, and with what capacity. In swarm robotics, determines the resilience and efficiency of collective coordination. Not synonymous with communication protocol or software architecture: it is the connectivity structure of the underlying graph.

_Related:_ scale-free networks, centralization, distribution, mesh, star
_Cross-references:_ [Complex Systems / Network Science](/thesaurus/complex-systems-network-science/)
_Key work:_ Barabási, A. L., & Albert, R. (1999). Emergence of scaling in random networks. _Science_, 286(5439), 509–512.

**Cosmos / Taxis** (Hayek, 1973)

Distinction between spontaneous order (cosmos) and designed order (taxis). A swarm that self-organizes without a central controller produces cosmos. The rules the engineer designs are minimal taxis: the set of conditions from which cosmos emerges. Confusing both levels is the most frequent conceptual error in autonomous robotics.

_Related:_ spontaneous order, self-organization, rules vs. outcomes
_Cross-references:_ [Praxeology / Austrian Political Economy](/thesaurus/praxeology-austrian-political-economy/), [Systems Engineering](/thesaurus/systems-engineering/), [Complex Systems / Network Science](/thesaurus/complex-systems-network-science/)
_Key work:_ Hayek, F. A. (1973). _Law, Legislation and Liberty, Vol. 1: Rules and Order_. University of Chicago Press.

**Emergent property**

Property of a system that cannot be deduced from the properties of its individual components or from the rules governing them. Flocking behavior is an emergent property: no individual rule specifies it. Distinct from a resultant property, which is deducible from the sum of parts.

_Related:_ emergence, non-linearity, complexity, synergy
_Cross-references:_ [Agent-Based Modeling (ABM)](/thesaurus/agent-based-modeling/), [Complex Systems / Network Science](/thesaurus/complex-systems-network-science/)
_Key work:_ Reynolds, C. W. (1987). Flocks, herds and schools. _ACM SIGGRAPH Computer Graphics_, 21(4), 25–34.

**Resilience**

Capacity of a system to maintain its function under perturbations and to recover from partial failures without total collapse. In robotic swarms, measured by the capacity to maintain the mission when some nodes fail or the network topology fragments. Distinct from robustness: robustness resists; resilience adapts.

_Related:_ graceful degradation, redundancy, fault tolerance, antifragility
_Cross-references:_ [Systems Engineering](/thesaurus/systems-engineering/), [Information Theory / Science and Technology](/thesaurus/information-theory-sci-tech/)
_Key work:_ Bonabeau, E., Dorigo, M., & Theraulaz, G. (1999). _Swarm Intelligence_. Oxford University Press.

**Distributed accountability**

Philosophical and legal problem arising when a collective system produces consequences with no identifiable decision node. From a praxeological standpoint, responsibility does not disappear with distribution: it is traceable to the human design, specification, and deployment decisions that shaped the system's rules and objectives.

_Related:_ agency, intentionality, systems design, responsibility
_Cross-references:_ [Praxeology / Austrian Political Economy](/thesaurus/praxeology-austrian-political-economy/)
_Key work:_ Mises, L. von (1949). _Human Action: A Treatise on Economics_. Yale University Press.

## References

Bonabeau, E., Dorigo, M., & Theraulaz, G. (1999). _Swarm Intelligence: From Natural to Artificial Systems_. Oxford University Press.

Dorigo, M., & Gambardella, L. M. (1997). Ant colony system. _IEEE Transactions on Evolutionary Computation_, 1(1), 53–66.

Grassé, P. P. (1959). La reconstruction du nid et les coordinations interindividuelles chez Bellicositermes natalensis et Cubitermes sp. _Insectes Sociaux_, 6(1), 41–80.

Hayek, F. A. (1973). _Law, Legislation and Liberty, Vol. 1: Rules and Order_. University of Chicago Press.

Reynolds, C. W. (1987). Flocks, herds and schools: A distributed behavioral model. _ACM SIGGRAPH Computer Graphics_, 21(4), 25–34.
