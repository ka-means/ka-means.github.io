---
layout: page
permalink: /repositories/
title: Repositories
description: Live-pulled public repositories from GitHub (ka-means personal account and the KahloGroup org), forks excluded, sorted by last updated.
nav: true
nav_order: 4
---

<div id="gh-repos-status">Loading repositories from the GitHub API&hellip;</div>
<div id="gh-repos-list" class="row row-cols-1 row-cols-md-3"></div>

<script>
(function () {
  var USERS = ["ka-means"];
  var ORGS = ["KahloGroup"];
  var HIDDEN_REPOS = ["ka-means/ka-means.github.io"];
  var statusEl = document.getElementById("gh-repos-status");
  var listEl = document.getElementById("gh-repos-list");

  function fetchAll(path, names) {
    return Promise.all(
      names.map(function (name) {
        return fetch("https://api.github.com/" + path + "/" + name + "/repos?per_page=100&type=owner")
          .then(function (res) {
            if (!res.ok) throw new Error(name + ": " + res.status);
            return res.json();
          })
          .catch(function (err) {
            console.error("Repositories page:", err);
            return [];
          });
      })
    ).then(function (results) {
      return [].concat.apply([], results);
    });
  }

  Promise.all([fetchAll("users", USERS), fetchAll("orgs", ORGS)])
    .then(function (both) {
      var repos = both[0].concat(both[1]);

      var seen = {};
      repos = repos.filter(function (repo) {
        if (!repo || repo.fork) return false;
        if (HIDDEN_REPOS.indexOf(repo.full_name) !== -1) return false;
        if (seen[repo.full_name]) return false;
        seen[repo.full_name] = true;
        return true;
      });

      repos.sort(function (a, b) {
        return new Date(b.pushed_at) - new Date(a.pushed_at);
      });

      if (repos.length === 0) {
        statusEl.textContent = "No repositories found (or the GitHub API rate limit was hit — try again shortly).";
        return;
      }

      statusEl.remove();

      repos.forEach(function (repo) {
        var col = document.createElement("div");
        col.className = "col mb-4";

        var card = document.createElement("div");
        card.className = "card h-100 hoverable";

        var body = document.createElement("div");
        body.className = "card-body";

        var title = document.createElement("h2");
        title.className = "card-title";
        var link = document.createElement("a");
        link.href = repo.html_url;
        link.target = "_blank";
        link.rel = "noopener";
        link.textContent = repo.full_name;
        title.appendChild(link);

        var desc = document.createElement("p");
        desc.className = "card-text";
        desc.textContent = repo.description || "";

        var meta = document.createElement("p");
        meta.className = "post-tags";
        var bits = [];
        if (repo.language) bits.push('<span><i class="fa-solid fa-circle fa-2xs"></i> ' + repo.language + "</span>");
        bits.push('<span><i class="fa-solid fa-star fa-sm"></i> ' + repo.stargazers_count + "</span>");
        meta.innerHTML = bits.join(" &nbsp;&middot;&nbsp; ");

        body.appendChild(title);
        body.appendChild(desc);
        body.appendChild(meta);
        card.appendChild(body);
        col.appendChild(card);
        listEl.appendChild(col);
      });
    })
    .catch(function (err) {
      console.error("Repositories page:", err);
      statusEl.textContent = "Couldn't load repositories from the GitHub API right now. Please try again later.";
    });
})();
</script>
