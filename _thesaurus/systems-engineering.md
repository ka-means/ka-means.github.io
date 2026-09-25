---
layout: page
title: "Systems Engineering"
description: Thesaurus of terms from the Engineering category — graceful degradation, cosmos/taxis applied to software, microservices, adaptive systems, and formal specification.
related_publications: false
permalink: /thesaurus/systems-engineering/
---

**Parent article:** [Engineering: Designing Conditions, Not Outcomes](/blog/2023/engineering-designing-conditions-not-outcomes/)

---

**Graceful degradation**

Capacity of a system to maintain its critical functions while losing peripheral ones in a predictable and recoverable way under stress or partial failure. Contrast: catastrophic failure, where one component's failure collapses the whole system. Biological systems, the internet, and markets exhibit this property; most enterprise software does not.

_Related:_ resilience, redundancy, fault tolerance, antifragility
_Cross-references:_ [Robotics / Swarm Systems](/thesaurus/robotics-swarm-systems/), [Information Theory / Science and Technology](/thesaurus/information-theory-sci-tech/), [Complex Systems / Network Science](/thesaurus/complex-systems-network-science/)
_Key work:_ Leiner, B. M., et al. (2009). A brief history of the Internet. _ACM SIGCOMM Computer Communication Review_, 39(5), 22–31.

**Cosmos / Taxis applied to software**

In systems engineering: the distinction between specifying the system's behavior (taxis) and specifying the conditions from which behavior emerges (minimal cosmos). Microservices are taxis in their interface contracts and cosmos in their aggregate behavior. Software architecture is progressively moving from the former to the latter.

_Related:_ emergent architecture, interface contracts, condition design
_Cross-references:_ [Praxeology / Austrian Political Economy](/thesaurus/praxeology-austrian-political-economy/), [Robotics / Swarm Systems](/thesaurus/robotics-swarm-systems/), [Complex Systems / Network Science](/thesaurus/complex-systems-network-science/)
_Key work:_ Hayek, F. A. (1973). _Law, Legislation and Liberty, Vol. 1_. University of Chicago Press.

**Microservices**

Architectural pattern where an application is built as a set of small, independent services communicating through well-defined APIs. Coordination emerges from interface contracts, not from central direction. The failure of one service does not propagate to the whole system. Cost: greater complexity in observability and orchestration.

_Related:_ distributed architecture, API, decoupling, service mesh
_Cross-references:_ [Complex Systems / Network Science](/thesaurus/complex-systems-network-science/)
_Key work:_ Fowler, M., & Lewis, J. (2014). Microservices. https://martinfowler.com/articles/microservices.html

**Adaptive systems**

Systems that modify their own parameters in response to environmental feedback without direct human intervention. Critical distinction: parameter adaptation (the system learns within a fixed architecture) versus architectural adaptation (the system modifies its own structure). Most current ML systems do the former; the latter remains an open problem.

_Related:_ machine learning, adaptive control, feedback, self-modification
_Cross-references:_ [Artificial Intelligence / Machine Learning](/thesaurus/ai-ml/)
_Key work:_ Jerne, N. K. (1974). Towards a network theory of the immune system. _Annals of Immunology_, 125C(1–2), 373–389.

**Formal specification**

Mathematically precise description of a system's expected behavior. In deterministic systems: sufficient to verify correctness. In probabilistic and emergent systems: insufficient, because the relevant behavior cannot be enumerated in advance. The boundary between formal specification and condition design is where software engineering becomes complex systems science.

_Related:_ formal verification, behavior model, contracts, preconditions
_Cross-references:_ [Agent-Based Modeling (ABM)](/thesaurus/agent-based-modeling/), [Artificial Intelligence / Machine Learning](/thesaurus/ai-ml/)
_Key work:_ Brooks, F. P. (1975). _The Mythical Man-Month_. Addison-Wesley.

## References

Brooks, F. P. (1975). _The Mythical Man-Month_. Addison-Wesley.

Fowler, M., & Lewis, J. (2014). Microservices. _martinfowler.com_. https://martinfowler.com/articles/microservices.html

Hayek, F. A. (1973). _Law, Legislation and Liberty, Vol. 1: Rules and Order_. University of Chicago Press.

Jerne, N. K. (1974). Towards a network theory of the immune system. _Annals of Immunology_, 125C(1–2), 373–389.

Leiner, B. M., Cerf, V. G., Clark, D. D., Kahn, R. E., Kleinrock, L., Lynch, D. C., … Wolff, S. (2009). A brief history of the Internet. _ACM SIGCOMM Computer Communication Review_, 39(5), 22–31.
