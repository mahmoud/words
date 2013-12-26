Python for Ruby developers
==========================

Ruby and Python are like language cousins:

* Focus on simple, readable syntax
* Dynamic, reflective, object-oriented, general-purpose
* Developed in the early/mid-90s
* Similar implementations (basic reference implementations in C: CPython, MRI/CRuby)

Python is big on having one obvious way of doing things. Explicit is
better than implicit, flat is better than nested, simple is better
than complex, complex is better than complicated, practicality beats
purity.

Ruby is a little more pure when it comes to object-orientedness, but
both are hybrid languages, combining imperative, object-oriented, and
functional constructs.

First differences you'll notice (syntax differences):

* Always call functions with parentheses, even if there are no
  arguments
* No monkey-patching or in-place extension of builtin types like
  string
* Python's module system is a little (very) different (but also, import instead of require)
* Python has list comprehensions, which are great
* Python is whitespace significant, no "end"s

  * In the same vein, Python has a style guide, PEP8, which means a
    really uniform set of expectations for syntax

Big similarities though:

Hash <-> Dict
Array <-> List
begin/rescue <-> try/except

REPL is really important. dir() and help() are your friends.

In practice
-----------

While Ruby is a general purpose language, the community is pretty
webdev-centric (though with Puppet and Chef there is an emerging
systems administration and operations aspect). Ruby and Python's
webdev community is about the same order of magnitude.

Python also has a great deal of academic use in everything from
physics to neurosciences. It's seeing rapidly expanding systems
administration with OpenStack. Used a lot in gaming (Civilization used
it at one point), Battlefield, Eve Online. Animation and rendering
(Disney, Industrial Light and Magic, etc.). Python's got a lot of GUI
libraries and works on Windows, too.

Python and Ruby both have "fast VMs" in the works (PyPy and
Rubinius/Topaz) as well as JVM-based runtimes (Jython and JRuby).

Big users of Python
-------------------

* YouTube
* Yelp
* Dropbox
* Disqus
* Quora
* Eventbrite
* NASA
* Rackspace
* Disney
* National Weather Service
* Wikipedia/Wikimedia
* PayPal

* Google, Apple, Yahoo, even the CIA all have some Python


Shoutoutz to Mike Leone for giving a great talk on this at the LA
RubyConf 2013: https://speakerdeck.com/mleone/python-for-ruby-programmers
