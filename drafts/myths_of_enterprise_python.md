# 9 Myths of Enterprise Python

Frequent readers of this blog are no doubt aware of the increasingly
diverse techno-pluralist environment here at PayPal. In past posts
we've showcased Java, JavaScript, Objective C, and Scala, but wouldn't
you know it, PayPal's also got a long history with C++, Ruby (with the
acquisition of Braintree), and you guessed it, Python. In this series
of posts, I'll be detailing how the eBay/PayPal Python community grew
from just under 25 engineers in 2011 to over 260 in 2014, starting
with a list of the most common concerns I have had to address over the
years of building Python support at PayPal, and now eBay.

Python has always been a language of choice for developers. Even when
there was no official support from management, developers go the extra
mile to be able to reap the rewards of Python development. Python has
enjoyed many years of grassroots usage and support from developers
across eBay; code archaeology has revealed signs of PayPal Python
usage dating back as early as Y2K. Today, Python is used for over 50
projects across eBay Inc., including:

 * Features and products, such as eBay Now
 * Operations and infrastructure, vis a vis OpenStack
 * Mid-tier services and applications, like the one used to set PayPal's prices
 * Monitoring agents and interfaces, used for several deployment and security use cases
 * Batch jobs
 *
 * Too many developer tools to count

## Myth #1: Python is not compiled

While not requiring a separate compiler toolchain like C++,
Python is in fact compiled to bytecode, much like Java and many other
compiled languages. Further compilation steps, if any, are at the
discretion of the runtime, be it CPython, PyPy, Jython/JVM,
IronPython/CLR, or some other process virtual machine.

## Myth #2: Python is a scripting language

Python can indeed be used for scripting, and is one of the forerunners
of the domain due to its simple syntax, cross-platform support, and
ubiquity among Linux, Macs, and other Unix machines.

In fact, Python may be one of the most flexible technologies among
general-use programming languages. To list just a few:

  1. Telephony infrastructure ([Twilio][twilio])
  2. Payments systems ([PayPal][paypal], [Balanced Payments][balanced])
  3. Neuroscience and psychology ([citation][neuroscience])
  4. Numerical analysis and engineering ([numpy][numpy] and [many more][numerical])
  5. Animation ([LucasArts][lucasarts], [Disney][disneytech], [Dreamworks][dreamworks])
  6. Gaming backends ([Eve Online][eve_online], [Second Life][second_life], [Battlefield][battlefield], and [so many others][other_games])
  7. Email infrastructure ([Mailman][mailman], [Mailgun][mailgun])
  8. Media storage and processing ([YouTube][youtube], [Instagram][instagram], [Dropbox][dropboxtech])
  9. Operations and systems management ([Rackspace][rackspace], [OpenStack][openstack])
  10. Natural language processing ([NLTK][nltk])
  11. Machine learning and computer vision ([scikit-learn][scikit], [Orange][orange], [SimpleCV][simplecv])
  12. Security and penetration testing ([so many][pentest])
  13. Big Data ([Disco][disco], [Hadoop support][hadoop])
  14. DNS ([BIND 10][bind10])

Not to mention websites and web services aplenty.

[twilio]: https://en.wikipedia.org/wiki/Twilio
[neuroscience]: http://www.frontiersin.org/neuroinformatics/researchtopics/Python_in_neuroscience/8
[paypal]: https://en.wikipedia.org/wiki/PayPal
[balanced]: https://www.balancedpayments.com/
[numpy]: https://en.wikipedia.org/wiki/NumPy
[numerical]: https://wiki.python.org/moin/NumericAndScientific
[lucasarts]: https://en.wikipedia.org/wiki/LucasArts
[disneytech]: http://www.disneyanimation.com/technology/opensource
[dreamworks]: https://en.wikipedia.org/wiki/DreamWorks_Animation
[eve_online]: https://en.wikipedia.org/wiki/Eve_Online
[second_life]: https://en.wikipedia.org/wiki/Second_Life
[battlefield]: https://en.wikipedia.org/wiki/Battlefield_(series)
[other_games]: https://wiki.python.org/moin/PythonGames
[mailman]: https://en.wikipedia.org/wiki/GNU_Mailman
[mailgun]: http://www.rackspace.com/mailgun
[youtube]: https://en.wikipedia.org/wiki/YouTube
[instagram]: http://instagram-engineering.tumblr.com/post/13649370142/what-powers-instagram-hundreds-of-instances
[dropboxtech]: https://tech.dropbox.com/
[rackspace]: https://en.wikipedia.org/wiki/Rackspace
[openstack]: http://www.openstack.org/
[nltk]: http://www.nltk.org/
[scikit]: http://scikit-learn.org/stable/
[orange]: http://orange.biolab.si/
[simplecv]: http://simplecv.org/
[pentest]: https://github.com/dloss/python-pentest-tools
[bind10]: http://www.isc.org/blogs/programming-languages-for-bind-10/
[disco]: http://discoproject.org/
[hadoop]: http://blog.cloudera.com/blog/2013/01/a-guide-to-python-frameworks-for-hadoop/

## Myth #3: Python is weakly-typed

Python is dynamically typed, and in fact more strongly-typed than
Java. Java has a split type system for primitives and objects, with
``null`` lying in a sort of gray area. On the other hand, modern
Python has a unified strong type system. And yes, the type of ``None``
is well-specified.

## Myth #4: Python is slow

First, a critical distinction: Python is a programming language, not a
runtime.

There are several Python implementations.

  1. [**CPython**][cpython] is the reference implementation, and also the most widely
     distributed and used.
  2. [**Jython**][jython] is a mature implementation of Python for usage with the JVM.
  3. [**IronPython**][ironpython] is Microsoft's Python for the Common Language Runtime, aka .NET.
  4. [**PyPy**][pypy] is an up-and-coming implementation of Python, with advanced
     features such as JIT compilation, incremental garbage collection,
     and more.

[cpython]: https://en.wikipedia.org/wiki/CPython
[jython]: https://en.wikipedia.org/wiki/Jython
[ironpython]: https://en.wikipedia.org/wiki/IronPython
[pypy]: https://en.wikipedia.org/wiki/PyPy

Each runtime has its own performance characteristics, and none of them
are slow per se. The more important point here is that it is a mistake
to assign performance assessments to a programming languages. Always
assess an application runtime, most preferably against a particular
use case.

Having cleared that up, here is a small selection of cases where
Python has offered significant performance advantages:

  1. Some SIMD use cases
  2. PyPy's JIT compilation achieves faster-than-C performance
  3. Disqus handles xxx requests on just yyy boxes

It would be easy to devote a whole post to high-performance Python and
the unique offerings of various Python runtimes, but if there is one
point to be made it is to emphasize the impact of developer
productivity on end-product performance.

Given enough time, a disciplined developer can execute the only proven
approach to achieving accurate and performant software:

  1. Engineer for correct behavior, including the development of respective tests
  2. Profile and measure performance, identifying bottlenecks
  3. Optimize, paying proper respect to the test suite and Amdahl's Law

It might sound simple, but even for seasoned engineers, this can be a
very time-consuming process. Python was designed from the ground up
with developer timelines in mind. In our experience, it's not uncommon
for Python projects to undergo three or more iterations in the time it
C++ and Java to do just one.

## Myth #5: Python does not scale

Scale has many definitions, but by any definition, YouTube is a web
site at scale. More than 1 billion unique visitors per month, over 100
hours of uploads per minute, and 20% of peak Internet bandwidth, all
with Python as a core technology. Dropbox, Disqus, Eventbrite, Twilio,
Instagram, EVE Online, Second Life, and, yes, eBay all have scaling
stories that prove scale is more than just possible with Python: it's
a pattern.

The key to success is simplicity and consistency. CPython, the primary
Python virtual machine, maximizes these characteristics, which makes
for a very predictable runtime. One would be hard pressed to find
Python programmers concerned about garbage collection pauses. With
strong platform and networking support, Python naturally lends itself
to horizontal scalability.

Additionally, scaling is all about measurement and iteration. Python
is built with profiling and optimization in mind. See Myth #4 for more
details on how to vertically scale Python.

## Myth #6: Python is a new language

What with all the startups using it and kids learning it these days,
it's easy to see how this myth still persists. Python is actually 23
years old, originally released in 1991, 4 years before Java. A
now-famous early usage of Python was in 1996: Google's first
successful web crawler.

If you're curious about the long history of Python, Guido van Rossum,
Python's creator, [has taken the care to tell the whole
story][python_history].

[python_history]: http://python-history.blogspot.com/2009/01/introduction-and-overview.html

## Myth #7: Python is not for big projects

Myth #5 discussed Python at scale, but there is another aspect to
scaling worth discussing: people. While Instagram reached hundreds of
millions of hits a day, at the time of Facebook's billion dollar
purchase, the whole company was still only a group of a dozen or so
people. Dropbox and other teams were similarly lean. So, can Python
scale to large teams?

Bank of America actually has over 2,000 Python developers, so you
better believe it buster. Same goes for YouTube. Big products and big
teams use Python every day. Python has excellent modularity and
packaging characteristics, but beyond a certain point, much of the
advice stays the same: Tooling, conventions, and code review make big
projects a reality.

Luckily, Python starts with a good baseline on those fronts as
well. We use PyFlakes and other tools to perform static analysis of
Python code before it gets checked in, as well as adhering to PEP8,
Python's language-wide base style guide.

Finally, it should be noted that, in addition to the scheduling
speedups mentioned in Myth #4 and #5, projects using Python generally
require fewer developers, as well. Our most common success story
starts with a Java or C++ project slated to take a team of 3-5
developers somewhere between 2-6 months, and ends with a single
motivated developer completing the project in 2-6 weeks.

A miracle for some, but a fact of modern development, and often a
necessity of competitive business.

## Myth #8: Python is not secure

Python's lightweight nature may not make it seem formidable, but the
intuition here can be misleading. One central tenet of security is to
present as small a target as possible, and CPython achieves this by
being a very simple and easily-auditable VM. In fact, a recent
analysis by Fortify Software gave CPython their highest rating.

Python also has an extensive array of open-source, industry-standard
security libraries. At PayPal we find that a combination of PyOpenSSL,
PyCrypto, and hashlib cover all of PayPal's diverse security and
performance needs.

## Myth #9: Python programmers are scarce

There is some truth to this myth. There are not as many Python
developers as PHP or Java developers, mostly due to a combined
interaction of industry demand and education, though trends in
education suggest that this may change.

That said, Python developers are far from scarce. There are millions
worldwide, as evidenced by the dozens of Python conferences, tens of
thousands of StackOverflow questions, and companies like YouTube, Bank
of America, and LucasArts/Dreamworks employing Python developers by
the hundreds and thousands. At eBay we have over 200 developers who
use Python on a regular basis, so what's the trick?

Well, one does not need to find what one can create. Python is
exceptionally easy to learn, and is a first programming language for
children and university students alike. At eBay, it only takes one
week to show real results for a new Python programmer, and they often
really start to shine as quickly as 2-3 months, all made possible by
the Internet's rich cache of interactive tutorials, books,
documentation, and open-source codebases.

Another important factor to consider is that projects using Python
simply do not require as many developers as other projects. As
mentioned in Myth #7, lean, effective teams like Instagram are a
common trope in Python projects, and this has certainly been our
experience at eBay and PayPal.
