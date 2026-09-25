---
layout: post
title: "Sci-Tech: The Difference Between Data and Knowledge"
date: 2026-03-11 09:00:00-0000
description: "A forecast that tells you something you already knew carries zero information regardless of how many bytes it occupies."
categories: [sci-tech]
related_posts: false
---

Claude Shannon published "A Mathematical Theory of Communication" in 1948. He was at Bell Labs working on the problem of transmitting signals over noisy channels, and the mathematics he developed established information theory. The central concept, entropy, came directly from thermodynamics. Ludwig Boltzmann defined statistical entropy in the 1870s as a measure of disorder in physical systems. Shannon recognized that the same mathematics described uncertainty in communication systems and imported it directly. Information theory did not emerge from engineering. It emerged from physics, passed through cryptography (Shannon worked on wartime ciphers), and arrived at communications.

Shannon entropy measures the average unpredictability of a signal: the minimum number of bits needed to encode a message without losing any of it. A perfectly predictable signal has zero entropy. A completely random signal has maximum entropy. Real signals sit between those extremes. Compression algorithms work by finding and removing predictable structure, transmitting only the genuinely uncertain parts. This is not a heuristic. It is the mathematical lower bound on how much compression is possible without information loss.

The distinction between data and information follows from this directly. Data is the raw signal. Information, in Shannon's technical sense, is the reduction in uncertainty that the signal produces for a specific receiver with specific prior knowledge. A forecast that tells you something you already knew carries zero information regardless of how many bytes it occupies. A one-bit message that resolves genuine uncertainty carries high information precisely because of its brevity.

Hayek's 1945 paper describes a structurally identical problem in economics. The knowledge relevant to economic coordination is not the kind that can be written in a report and transmitted to a central office. It is local, tacit, and situational: the specific circumstances of time and place, the momentary quality of a batch of materials, the particular opportunity that will disappear if not acted on immediately. This knowledge cannot be aggregated into data without being destroyed. What prices do is transmit the relevant signal, the change in relative scarcity, without requiring anyone to articulate or centralize the underlying knowledge that generated that signal. The market is, in this sense, a distributed information compression system that operates without anyone designing it.

The current assumption that accumulating more data automatically produces more knowledge and better decisions repeats the central planner's error in a technological register. Data that is redundant, irrelevant, or disconnected from any specific question contributes noise rather than signal. Interconnected systems do generate new noise sources as they grow, and managing those sources requires explicit engineering effort. The claim that noise grows exponentially with scale is not a general result; it depends on system design and filtering mechanisms. The accurate claim is that scale makes noise management a first-order engineering problem rather than an afterthought.

Graceful degradation is, from my point of view, the most undervalued concept in this space. It refers to a system's capacity to maintain its most critical functions under stress while losing peripheral functions in a predictable and recoverable way. Biological systems degrade gracefully: a damaged liver continues filtering, just less efficiently. The internet's routing protocols degrade gracefully: packets find alternate paths around failed nodes. Markets degrade gracefully: price signals adjust to disruptions and redirect resources continuously, without requiring any authority to activate the recovery process. Centrally designed systems tend not to degrade gracefully, because their specifications don't account for conditions the designer didn't anticipate, and failure in one component can cascade unpredictably through the whole.

The engineering challenge that matters is not building larger systems. It's building systems that fail the way good institutions fail: partially, predictably, and with recovery mechanisms that don't require a central authority to activate them.

## Questions worth investigating

1. Shannon entropy and Kolmogorov complexity both characterize information content but measure different things. What is the precise relationship between them, and why does it matter for signal analysis and data compression in practice?
2. Hayek's tacit knowledge and Shannon's entropy both point at something that resists explicit aggregation or articulation. Has there been a formal attempt to connect these two frameworks, and what would such a connection imply for distributed system design?
