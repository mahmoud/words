If I ever actually write a full-blown web "product" I can't see myself
using dinky lean-to templating engines like Jinja2, Mako, Django, or
ashes. It will likely be one or a combination of:

 1. DOM-oriented additive
 2. Layout-based, like good-old GUI programming
 3. Programmatic merge based, like Diazo

Developing something sizable purely based on the DOM-oriented approach
means lots of minutia handling. I'd probably use this in combination
with

The Layout approach comes with comforting abstractions, but the
comfort may be shortlived if you have to implement what's under the
abstractions.

Diazo is nice, and offers a nice workflow-practical compromise,
minimizing tedium and generating significant metadata. The setup is
kind of heavy, with an LXML dependency and XSLT baggage.
