---
layout: list
title: Available Carvings
---

{% assign carvings = site.carvings | where: 'available', 'true' %}
{% for carving in carvings %}
  {% include list_card.html carving=carving %}
{% endfor %}
