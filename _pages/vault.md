---
layout: default
permalink: /vault/
title: Vault
description: Notes, Colab notebooks, slides, and reports & concept maps.
nav: true
nav_order: 6
---

<div class="post">

  <div class="header-bar">
    <h1>Vault</h1>
    <h2>{{ page.description }}</h2>
  </div>

  <h2 id="notes"><a href="#notes">Notes</a></h2>
  <p>Wiki-style class/course notes, grouped by course.</p>
  {% assign notes_by_course = site.notes | group_by: "course" %}
  {% for course_group in notes_by_course %}
  <h3>{{ course_group.name }}</h3>
  <ul class="post-list">
    {% assign sorted_notes = course_group.items | sort: "date" | reverse %}
    {% for note in sorted_notes %}
    <li>
      <h3><a class="post-title" href="{{ note.url | relative_url }}">{{ note.title }}</a></h3>
      <p>{{ note.description }}</p>
    </li>
    {% endfor %}
  </ul>
  {% else %}
  <p>No notes yet.</p>
  {% endfor %}

  <hr>

  <h2 id="colab"><a href="#colab">Colab</a></h2>
  <p>Pointer entries to executable notebooks — the linked GitHub repo is the source of truth.</p>
  <ul class="post-list">
    {% assign colab_items = site.colab | sort: "title" %}
    {% for item in colab_items %}
    <li>
      <h3><a class="post-title" href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
      <p>{{ item.description }}</p>
    </li>
    {% else %}
    <p>No Colab entries yet.</p>
    {% endfor %}
  </ul>

  <hr>

  <h2 id="slides"><a href="#slides">Slides</a></h2>
  <p>Presentation decks, exported as PDF or embedded from Google Slides/SlideShare.</p>
  <ul class="post-list">
    {% assign slide_items = site.slides | sort: "title" %}
    {% for item in slide_items %}
    <li>
      <h3><a class="post-title" href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
      <p>{{ item.description }}</p>
    </li>
    {% else %}
    <p>No slide decks yet.</p>
    {% endfor %}
  </ul>

  <hr>

  <h2 id="books"><a href="#books">Books</a></h2>
  <p>Full books and other long-form documents.</p>
  <ul class="post-list">
    {% assign book_items = site.books | sort: "title" %}
    {% for item in book_items %}
    <li>
      <h3><a class="post-title" href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
      <p>{{ item.description }}</p>
    </li>
    {% else %}
    <p>No books yet.</p>
    {% endfor %}
  </ul>

  <hr>

  <h2 id="reports"><a href="#reports">Reports &amp; concept maps</a></h2>
  <p>Standalone reports and concept/mind maps not tied to a course or formal publication.</p>
  <ul class="post-list">
    {% assign report_items = site.reports | sort: "title" %}
    {% for item in report_items %}
    <li>
      <h3><a class="post-title" href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
      <p>{{ item.description }}</p>
    </li>
    {% else %}
    <p>No reports yet.</p>
    {% endfor %}
  </ul>

</div>
