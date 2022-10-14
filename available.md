---
layout: list
title: Available Carvings
description: >
  Interested in making a purchase or a swap? Get in touch with me at
  <a href="mailto:hillel@hillelarnold.com">hillel@hillelarnold.com</a>.
---

{% assign carvings = site.carvings | where: 'available', 'true' %}
{% for carving in carvings %}
  {% include list_card.html carving=carving %}
{% endfor %}
