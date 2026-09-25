---
layout: post
title: "Presenting: Andrei Kolmogorov"
date: 2026-09-25 00:00:00-0000
description: "There are mathematicians who solve problems. And there are mathematicians who change the way everyone else asks questions. Andrei Nikolaevich Kolmogorov was the second kind."
categories: [presenting]
related_posts: false
---

<div class="portrait-duotone">
  <img src="{{ '/assets/img/andrei-kolmogorov.png' | relative_url }}" alt="Portrait of Andrei Kolmogorov" />
</div>

There are mathematicians who solve problems. And there are mathematicians who change the way everyone else asks questions. **Andrei Nikolaevich Kolmogorov was the second kind.**

He was born in 1903 in Tambov, Russia, and died in 1987 in Moscow, having lived through almost the entire twentieth century and shaped a significant part of it. His list of contributions to mathematics is unusual in its breadth: he **axiomatized probability theory in 1933**, the work that gives every statistician alive today the ground they stand on; he worked on turbulence, classical mechanics, topology, and intuitionistic logic. He was not a deep specialist in one area. He was someone who moved between fields and reorganized them from the inside.

The work that puts his name in this article came late in his career. In 1965, when he was already one of the most respected mathematicians in the world, he published a short and dense paper titled **"Three Approaches to the Quantitative Definition of Information."** In it he proposed something that sounds simple but carries enormous consequences: **measuring the information contained in an individual object, not in a distribution of objects**, based on the length of the shortest program capable of reproducing it.

That is Kolmogorov complexity. **The amount of irreducible information in something, measured by how short its complete description can be.**

## The problem Kolmogorov wanted to solve

To understand why it mattered, you need to understand what came before.

In 1948, Claude Shannon published his mathematical theory of communication and defined entropy as a measure of the **average uncertainty of an information source**. Shannon was answering a very concrete and very practical question: how many bits do I need to transmit messages from this source without losing anything? It was a measure over populations of messages, over distributions, over averages.

**What Shannon could not do was tell you anything about one specific object.** If I hand you a specific bit sequence, Shannon's theory does not tell you whether that particular sequence is simple or complex. It tells you how much space it occupies on average if it came from a certain source. That is not the same thing.

Kolmogorov wanted a definition of information and randomness that worked for individual objects. He wanted to be able to say: **this particular string is random, or this other one has structure**, without needing to assume it came from any known source. And the answer he found was elegant: **the complexity of an object is the length of the shortest program that can produce it on a universal computer.**

If the program is short, the object has structure. It is predictable. It is compressible. If the shortest program is as long as the object itself, the object is irreducible. That, said Kolmogorov, is what it means to be **truly random**.

## What it looks like in practice

Take concrete examples, because here the intuition matters.

A string of ten thousand zeros has **very low complexity**. The program that generates it is "print ten thousand zeros." That fits in one line.

An alternating sequence, 010101 repeated five thousand times, is the same. "Repeat 01 five thousand times." Still very short.

Now take a sequence generated at random, with no underlying pattern. The shortest program to reproduce it is essentially the sequence itself: "print this." There is no more compact description. **That is high Kolmogorov complexity. That is randomness in the most rigorous sense.**

The case I find most interesting is the number pi. Its decimals look chaotic: 3.14159265358979... no apparent periodicity, no repetition. But **pi has very low Kolmogorov complexity**, because there is a relatively short algorithm that generates every single digit with arbitrary precision. **The appearance of disorder is not the same as irreducible disorder.**

This formally distinguishes two things everyday language conflates: something can look complex without being so, if its generative rule is simple. And something can look ordered without being so, if its structure is shallow and goes nowhere. **Kolmogorov complexity measures the depth of structure, not its appearance.**

## The story has three protagonists

Kolmogorov did not arrive at this idea alone, and saying so honestly matters.

**Ray Solomonoff**, an American mathematician, published first. Between 1960 and 1964 he developed what we now call algorithmic probability or Solomonoff induction: a framework for assigning probabilities to hypotheses without assuming prior knowledge of the domain. His motivation was artificial intelligence: he wanted a truly universal way to predict. He got there first, though his name did not stick.

**Kolmogorov arrived in 1965** from a more fundamental angle. He was not interested in prediction but in definition. He wanted to know what it means for something to be random, in a strict and unambiguous sense. His formulation was the cleanest mathematically, and his reputation was enormous, so the concept carries his name.

**Gregory Chaitin** arrived independently, as an undergraduate student, around the same time as Kolmogorov. He later connected this theory to the halting problem, showed its deep philosophical implications, and introduced the **Omega number**: an incomputable constant that encodes the probability that a random program halts. Chaitin pushed the field into territory where mathematics and philosophy meet.

The correct name for all of this is **algorithmic information theory, founded by all three**. But the name that circulates is Kolmogorov complexity.

## The practical problem: it cannot be computed

Here we have to be direct: **the Kolmogorov complexity of an arbitrary string is uncomputable.** Not in the sense of being very hard. In the sense that no program can calculate it exactly in the general case. Verifying that a program is the shortest requires confirming that no shorter program halts producing the same output, and that verification runs directly into the halting problem, which is undecidable.

**What you can do is approximate it.** Any real compression algorithm, gzip, bzip2, LZMA, xz, gives you an upper bound on the Kolmogorov complexity of whatever you feed it. The better the compressor, the tighter the bound. And that approximation is enough to be genuinely useful in the real world.

## Where his ideas live today

Kolmogorov's trace is in more places than most practitioners recognize.

The tool most directly derived from his work is the **Normalized Compression Distance**, developed by Cilibrasi and Vitányi in 2005. The idea is simple: compress two objects separately, then compress them together. If they share structure, the combined file will be much smaller than the sum of the two separate ones. The ratio between those lengths gives a **similarity measure that requires no hand-crafted features, no domain knowledge, and works with any type of data that can be represented as bytes.**

In **cybersecurity**, NCD is used to classify malware. Two samples that share code or logic compress well together even when obfuscated. The compressor captures structural similarity that a human analyst would take hours to find.

In **genomics**, it builds phylogenetic trees without traditional sequence alignment. Two genomes that share evolutionary history compress well together. NCD reconstructs evolutionary relationships between species or virus strains simply by measuring how well pairs compress. A method Kolmogorov did not design for biology, but that biology found useful.

In **authorship attribution**, it identifies stylistic patterns the author themselves cannot consciously articulate. Writing style is structure, and structure compresses. Two texts by the same author compress better together than texts by different authors. The same applies to plagiarism detection.

The **Minimum Description Length principle**, formalized by Jorma Rissanen in the 1970s, carries the same intuition into statistical learning: given a dataset, prefer the model that lets you describe the data most briefly when you count both the model and the data. **This formally justifies why simpler models generalize better.** Modern regularization in machine learning is an approximate implementation of this principle, though few practitioners frame it that way.

And then there is the connection I find most fertile and least explored: if prices are, as **Hayek** argued, a mechanism for compressing dispersed tacit knowledge into a signal, then Kolmogorov complexity offers a way to ask **how much information a price series is actually encoding at any given moment**. A price that responds to a real change in the relative scarcity of a good carries information in the algorithmic sense. A price driven by speculative noise does not. The two look identical on a chart. They do not look identical to a compressor with access to the underlying data. **Nobody has fully developed that connection yet.**

## Why it matters beyond the technical

What Kolmogorov did, at its core, was give rigorous mathematical form to something philosophers had been saying imprecisely for centuries: **the simplest explanation is the best one. Occam's razor was not mathematically definable before 1965. With Kolmogorov complexity, it is.**

That has consequences beyond file compression. It means the notion of simplicity, of elegance, of structure, can be treated formally. It means the question "how complex is this phenomenon really" has an answer in principle, even if not always computable in practice. And it means that randomness, which for centuries was a philosophically slippery concept, now has a precise definition: **random is what cannot be compressed.**

Kolmogorov did not live to see most of the applications of his work. But he left the framework. Everything else was just finding uses for it.

## Questions worth investigating

1. If price series compress tacit knowledge in the Hayekian sense, can Kolmogorov complexity give us a formal measure of how much real information a price carries at different time scales? What would that reveal about market efficiency that current measures miss?
2. Could an MDL constraint on reward function complexity help prevent specification gaming in reinforcement learning?
3. Kolmogorov complexity is uncomputable but approximable. What are the formal bounds on how far a real compressor can be from the true complexity of a string, and does that approximation gap matter in practice for genomics and cybersecurity applications?

## References

Chaitin, G. J. (1966). On the length of programs for computing finite binary sequences. _Journal of the ACM_, 13(4), 547–569.

Cilibrasi, R., & Vitányi, P. M. B. (2005). Clustering by compression. _IEEE Transactions on Information Theory_, 51(4), 1523–1545.

Kolmogorov, A. N. (1965). Three approaches to the quantitative definition of information. _Problems of Information Transmission_, 1(1), 1–7.

Li, M., & Vitányi, P. M. B. (2008). _An Introduction to Kolmogorov Complexity and Its Applications_ (3rd ed.). Springer.

Rissanen, J. (1978). Modeling by shortest data description. _Automatica_, 14(5), 465–471.

Solomonoff, R. J. (1964). A formal theory of inductive inference. _Information and Control_, 7(1), 1–22.
