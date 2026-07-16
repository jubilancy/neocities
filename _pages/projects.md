---
layout: blog
title: Projects
subtitle: Some things I'm proud of...
permalink: /projects/
---

{% for project in site.projects %}
{% assign loopindex = forloop.index | modulo: 2 %}
{% if loopindex == 1 %}
{% assign evenodd = '' %}
{% else %}
{% assign evenodd = 'projecteven' %}
{% endif %}
<div class="projectcontainer">
<a href="{{project.url}}"><div class="projectdiv {{evenodd}}">
<img src="{{project.heroimage}}" />
<div class="projecttitle">{{project.title}}<br>
<span>{{project.subtitle}}</span><br><br>
<p class="mobilehidden">Learn more →</p>
</div>
</div></a>
</div>

{% endfor %}


