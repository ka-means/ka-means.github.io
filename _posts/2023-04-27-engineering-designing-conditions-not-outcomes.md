---
layout: post
title: "Engineering: Designing Conditions, Not Outcomes"
date: 2023-04-27 09:00:00-0000
description: "The engineer's job is shifting from writing correct behavior to designing the conditions under which correct behavior tends to emerge."
tags: [Engineering]
categories: [engineering]
related_posts: false
---

Friedrich Hayek distinguished two types of order. A taxis is designed: someone planned it, specified it, and it behaves according to that specification. A cosmos is emergent: it arose from individuals following local rules, and no one planned the overall structure. A factory assembly line is a taxis. The common law, which evolved from accumulated case decisions rather than legislative design, is a cosmos. The market is a cosmos. Language is a cosmos. Nobody designed English. It emerged from millions of speakers making local choices over centuries.

For most of computing history, software was unambiguously taxis. Every branch specified, every output determined, every behavior planned. The mental model was: if A, then B. It was precise, testable, and fragile. Change one assumption and the whole structure needed renegotiation.

That model remains appropriate for systems with stable and fully enumerable requirements. But it has become inadequate for a class of problems that grew rapidly in the last decade: systems operating in dynamic environments, interacting with unpredictable users, needing to maintain service while being continuously modified.

The response has been a gradual, mostly tacit, shift from specifying behavior to specifying conditions. Continuous deployment pipelines don't rewrite code autonomously. They automate the testing and release process, shrinking the feedback loop between writing a change and seeing it in production. Microservices replace a single monolithic program with many small services communicating through well-defined interfaces. When one fails, the others continue. The system degrades gracefully rather than collapsing completely. These are not autonomous systems. They are engineering disciplines that acknowledge the designer's inability to anticipate every future state.

The biological borrowings in this evolution are specific and traceable. The internet's packet routing was designed to route around damage, a property directly inspired by the resilience of neural networks. ARPA's original brief asked for a communication network that could survive partial destruction. The solution, distributed routing with no central coordinator, was informed by research on how biological systems maintain function under damage. Immune-system-inspired algorithms apply the principle of adaptive, distributed threat response to network security. These are not metaphors. Engineers looked at systems that had been selected for resilience over millions of years and asked what mechanisms produced that resilience.

The systems that genuinely modify their own parameters based on feedback, recommendation engines, adaptive control systems, anomaly detectors that recalibrate on what they observe, are doing something meaningfully different from a conventional program. They are not following a fixed rule. They are refining the rule based on experience. That changes what the engineer's job is: from writing correct behavior to designing the conditions under which correct behavior tends to emerge and incorrect behavior tends to be corrected.

From my point of view, the engineering temperament trained on deterministic systems consistently underestimates how much order can arise without top-down specification, and overestimates how much control top-down specification actually delivers. Real systems are always more complex than their specifications. The question is whether you design for that gap or pretend it doesn't exist and call what falls through it a bug.

## Questions worth investigating

1. Hayek's cosmos/taxis distinction was developed for social systems. Has it been formally applied in distributed systems theory or software architecture, and with what results?
2. Beyond neural networks and immune systems, which biological resilience mechanisms have been most productively formalized in distributed computing architectures?
