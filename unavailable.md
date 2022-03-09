---
layout: list
title: Unavailable Carvings
---

{% assign carvings = site.carvings | where: 'available', 'false' %}
{% for carving in carvings %}
  {% include list_card.html carving=carving %}
{% endfor %}
