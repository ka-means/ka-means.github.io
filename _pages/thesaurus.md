---
layout: default
permalink: /thesaurus/
title: Thesaurus
description: A glossary of terms developed across the blog's eight article categories, cross-referenced as a conceptual map.
nav: true
nav_order: 8
---

<div class="post">

  <div class="header-bar">
    <h1>Thesaurus</h1>
    <h2>{{ page.description }}</h2>
  </div>

  <p>Each category below develops the key terms introduced in its parent blog article. Every term entry names a "Key work," the founding or most important reference for that concept, and every category closes with its own References section. Cross-references between categories work as a conceptual map: follow a term from one category to a related term in another, and the citations chain with it.</p>

  <ul class="post-list">
    {% assign thesaurus_items = site.thesaurus | sort: "title" %}
    {% for item in thesaurus_items %}
    <li>
      <h3><a class="post-title" href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
      <p>{{ item.description }}</p>
    </li>
    {% else %}
    <p>No thesaurus categories yet.</p>
    {% endfor %}
  </ul>

</div>
