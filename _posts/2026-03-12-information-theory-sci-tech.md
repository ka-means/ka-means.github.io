---
layout: post
title: "Information Theory / Science and Technology"
date: 2026-03-12 09:00:00-0000
description: "Thesaurus of terms from the Sci-Tech category — Shannon entropy, Kolmogorov complexity, noise vs. signal, graceful degradation, data vs. knowledge, and informational resilience."
categories: [thesaurus]
related_posts: false
---

**Parent article:** [Sci-Tech: The Difference Between Data and Knowledge](/blog/2026/sci-tech-the-difference-between-data-and-knowledge/)

---

**Shannon entropy**

Measure of the average uncertainty or unpredictability of an information source. H = −Σ p(x) log p(x). Quantifies the minimum number of bits needed to encode the average output of the source without loss. Origin: imported from Boltzmann's statistical thermodynamic entropy (1870s) by Shannon (1948). A perfectly predictable signal has H = 0. A uniform distribution maximizes H.

_Related:_ information, bits, encoding, compression, redundancy
_Cross-references:_ [Complex Systems / Network Science](/blog/2022/complex-systems-network-science/) (thermodynamic entropy of Prigogine)
_Key work:_ Shannon, C. E. (1948). A mathematical theory of communication. _Bell System Technical Journal_, 27(3–4), 379–423.

**Kolmogorov complexity** (algorithmic complexity)

Length of the shortest program in a universal programming language that can produce a given string. Distinct from Shannon entropy at a crucial point: measures the complexity of a specific string, not the average uncertainty of a source. A truly random string has maximum Kolmogorov complexity (it cannot be compressed); it also has maximum Shannon entropy. A highly structured string can have low Kolmogorov complexity and high Shannon entropy if its generating rule is simple but produces much variety.

_Related:_ Shannon entropy, algorithmic information theory, compression, Chaitin
_Cross-references:_ none direct
_Key work:_ Kolmogorov, A. N. (1965). Three approaches to the quantitative definition of information. _Problems of Information Transmission_, 1(1), 1–7.

**Noise vs. signal**

Noise is not an objective property of a transmission: it is the component of a signal that carries no information relevant to the receiver in the context of their specific question. The same datum can be noise for one receiver and signal for another. This distinction is why "more data" does not imply "more knowledge": additional data may be noise, and noise raises the cost of extracting the signal.

_Related:_ Shannon entropy, filtering, compression, Goodhart's Law
_Cross-references:_ [Artificial Intelligence / Machine Learning](/blog/2025/ai-ml/)
_Key work:_ Wiener, N. (1948). _Cybernetics: Or Control and Communication in the Animal and the Machine_. MIT Press.

**Graceful degradation** (information theory context)

Capacity of a communication or network system to maintain the transmission of the most critical information when the channel or network degrades, sacrificing less essential layers in a predictable way. Example: progressive JPEG encoding, which allows reconstructing a low-quality version of the whole before all data is received. Principle the internet implements in its routing protocol.

_Related:_ resilience, progressive encoding, prioritization, redundancy
_Cross-references:_ [Systems Engineering](/blog/2023/systems-engineering/), [Robotics / Swarm Systems](/blog/2023/robotics-swarm-systems/)
_Key work:_ Leiner, B. M., et al. (2009). A brief history of the Internet. _ACM SIGCOMM Computer Communication Review_, 39(5), 22–31.

**Data vs. knowledge**

In Shannon's technical sense: data is the raw signal; knowledge is the reduction of uncertainty that signal produces for a specific receiver with specific prior knowledge. Parallel to Hayek's distinction between information dispersed among individual agents and data aggregated in a central office: the latter is not equivalent to the former. Aggregating dispersed knowledge into data destroys the dimension that made it informative.

_Related:_ Shannon entropy, tacit knowledge, signal, epistemic reduction
_Cross-references:_ [Praxeology / Austrian Political Economy](/blog/2025/praxeology-austrian-political-economy/)
_Key work:_ Hayek, F. A. (1945). The use of knowledge in society. _American Economic Review_, 35(4), 519–530.

**Informational resilience**

Capacity of a system to maintain the transmission of critical information and recover from perturbations without requiring a central authority to activate the recovery. The internet was designed with this principle explicitly (ARPANET). Markets exhibit this property emergently: price signals adjust to disruptions and redirect resources continuously, without any authority activating the process.

_Related:_ distributed routing, redundancy, graceful degradation, spontaneous order
_Cross-references:_ [Complex Systems / Network Science](/blog/2022/complex-systems-network-science/), [Praxeology / Austrian Political Economy](/blog/2025/praxeology-austrian-political-economy/)
_Key work:_ Shannon, C. E. (1948). A mathematical theory of communication. _Bell System Technical Journal_, 27(3–4), 379–423.

## References

Boltzmann, L. (1877). Über die Beziehung zwischen dem zweiten Hauptsatze der mechanischen Wärmetheorie und der Wahrscheinlichkeitsrechnung. _Wiener Berichte_, 76, 373–435.

Hayek, F. A. (1945). The use of knowledge in society. _American Economic Review_, 35(4), 519–530.

Kolmogorov, A. N. (1965). Three approaches to the quantitative definition of information. _Problems of Information Transmission_, 1(1), 1–7.

Shannon, C. E. (1948). A mathematical theory of communication. _Bell System Technical Journal_, 27(3–4), 379–423, 623–656.

Wiener, N. (1948). _Cybernetics: Or Control and Communication in the Animal and the Machine_. MIT Press.
