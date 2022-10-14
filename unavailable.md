---
layout: list
title: Unavailable Carvings
description: >
  I no longer have these in my possession but under certain circumstances I
  might consider trying to copy a piece. Get in touch with me at
  <a href="mailto:hillel@hillelarnold.com">hillel@hillelarnold.com</a>.
---

{% assign carvings = site.carvings | where: 'available', 'false' %}
{% for carving in carvings %}
  {% include list_card.html carving=carving %}
{% endfor %}
