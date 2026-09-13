---
layout: default
permalink: /media/
title: Media
description: Curated third-party learning resources, and my own recorded talks and podcast appearances.
nav: true
nav_order: 5
display_categories: [complex-systems, econ-politics, sci-tech, engineering]
---

<div class="post">

  <div class="header-bar">
    <h1>Media</h1>
    <h2>{{ page.description }}</h2>
  </div>

{% if page.display_categories and page.display_categories.size > 0 %}

  <div class="tag-category-list">
    <ul class="p-0 m-0">
      {% for category in page.display_categories %}
      <li>
        <a href="{{ category | slugify | prepend: '/media/tag/' | relative_url }}">{{ category }}</a>
      </li>
      {% unless forloop.last %}<p>&bull;</p>{% endunless %}
      {% endfor %}
    </ul>
  </div>
  {% endif %}

{% assign curated_items = site.media | where: "source_type", "curated" | sort: "date" | reverse %}
{% assign original_items = site.media | where: "source_type", "original" | sort: "date" | reverse %}

  <h2 class="mt-4">Curated: Worth Your Time</h2>
  <p class="text-muted">
    A personal mapping of classes, talks, videos, and podcasts on complex systems, robotics, engineering, information
    technology, mathematics, and economics/social sciences — things I've found genuinely valuable. This is a curation
    and pointer list only: 100% of the credit and citation for this work belongs to the original authors and sources
    linked from each card below.
  </p>

  <div class="row row-cols-1 row-cols-md-2">
    {% for item in curated_items %}
    <div class="col mb-4">
      <div class="card h-100 hoverable">
        <div class="card-body">
          <span class="post-tags">
            {% if item.media_type == "podcast" %}<i class="fa-solid fa-podcast"></i> Podcast{% elsif item.media_type == "course" %}<i class="fa-solid fa-graduation-cap"></i> Class{% else %}<i class="fa-solid fa-video"></i> Video{% endif %}
          </span>
          <h2 class="card-title">
            <a href="{{ item.source_url }}" target="_blank" rel="noopener">{{ item.title }}</a>
          </h2>
          <p class="card-text">{{ item.description }}</p>
          <p class="card-text"><small class="text-muted">Source: {{ item.source_name }}{% if item.source_author %} &middot; {{ item.source_author }}{% endif %}</small></p>
          {% if item.tags.size > 0 %}
          <p class="post-tags">
            {% for topic in item.tags %}
            <span class="category-badge">{{ topic }}</span>
            {% endfor %}
          </p>
          {% endif %}
        </div>
      </div>
    </div>
    {% else %}
    <p>No curated resources yet.</p>
    {% endfor %}
  </div>

  <h2 class="mt-5">My Own Media</h2>
  <p class="text-muted">Podcast episodes and recorded talks/presentations that I've authored or delivered myself.</p>

  <div class="row row-cols-1 row-cols-md-2">
    {% for item in original_items %}
    <div class="col mb-4">
      <a href="{{ item.url | relative_url }}" style="text-decoration: none;">
        <div class="card h-100 hoverable">
          <div class="card-body">
            <span class="post-tags">
              {% if item.media_type == "podcast" %}<i class="fa-solid fa-podcast"></i> Podcast{% else %}<i class="fa-solid fa-video"></i> Video{% endif %}
            </span>
            <h2 class="card-title">{{ item.title }}</h2>
            <p class="card-text">{{ item.description }}</p>
            {% if item.tags.size > 0 %}
            <p class="post-tags">
              {% for topic in item.tags %}
              <span class="category-badge">{{ topic }}</span>
              {% endfor %}
            </p>
            {% endif %}
          </div>
        </div>
      </a>
    </div>
    {% else %}
    <p>No original media yet.</p>
    {% endfor %}
  </div>

</div>
