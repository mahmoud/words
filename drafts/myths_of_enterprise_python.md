# 9 Myths of Enterprise Python

Frequent readers of this blog are no doubt aware of the increasingly
diverse techno-pluralist environment here at PayPal. In past posts
we've showcased Java, JavaScript, Objective C, and Scala, but wouldn't
you know it, PayPal's also got a long history with C++, Ruby (with the
acquisition of Braintree), and you guessed it, [Python][python]. In
this series of posts, I'll be detailing how the eBay/PayPal Python
community grew from just under 25 engineers in 2011 to over 260 in
2014, starting with a list of the most common concerns I have had to
address over the years of building Python support at PayPal, and now
eBay.

Python has always been a language of choice for developers. Even when
there was no official support from management, developers went the
extra mile to be able to reap the rewards of Python
development. Python has enjoyed many years of grassroots usage and
support from developers across eBay, Inc.; code archaeology has
revealed signs of PayPal Python usage dating back as early as the year
2000.

Today, Python is used for over 50 projects across eBay, Inc.,
including:

  * Features and products, such as [eBay Now][ebay_local] and [RedLaser][redlaser]
  * Operations and infrastructure, both [OpenStack][openstack] and proprietary
  * Mid-tier services and applications, like the one used to set PayPal's prices
  * Monitoring agents and interfaces, used for several deployment and security use cases
  * Batch jobs for data import, price adjustment, and more
  * And far too many developer tools to count

[python]: https://www.python.org/
[ebay_local]: http://www.ebay.com/lcl/
[redlaser]: http://redlaser.com/

## Myth #1: Python is not compiled

While not requiring a separate compiler toolchain like C++, Python is
in fact compiled to bytecode, much like Java and many other compiled
languages. Further compilation steps, if any, are at the discretion of
the runtime, be it CPython, PyPy, Jython/JVM, IronPython/CLR, or some
other process virtual machine. See Myth #4 for more info.

## Myth #2: Python is a scripting language

Python can indeed be used for scripting, and is one of the forerunners
of the domain due to its simple syntax, cross-platform support, and
ubiquity among Linux, Macs, and other Unix machines.

In fact, Python may be one of the most flexible technologies among
general-use programming languages. To list just a few:

  1. Telephony infrastructure ([Twilio][twilio])
  2. Payments systems ([PayPal][paypal], [Balanced Payments][balanced])
  3. Neuroscience and psychology ([citation][neuroscience])
  4. Numerical analysis and engineering ([numpy][numpy], [numba][numba], and [many more][numerical])
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
[numba]: http://numba.pydata.org/
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

Python's type system is characterized by strong, dynamic
typing. [Wikipedia can explain more][type_systems].

Not that it is a competition, but, fun fact, Python is more
strongly-typed than Java. Java has a split type system for primitives
and objects, with ``null`` lying in a sort of gray area. On the other
hand, modern Python has a unified strong type system, where the type
of ``None`` is well-specified. Furthermore, the JVM itself is also
dynamically-typed, as it [traces its roots back][jvm_history] to an
implemention of a Smalltalk VM acquired by Sun.

[Python's type system][python_data_model] is very nice, but for
enterprise use there are much bigger concerns at hand.

[type_systems]: https://en.wikipedia.org/wiki/Type_system
[jvm_history]: https://en.wikipedia.org/wiki/HotSpot#History
[python_data_model]: https://docs.python.org/2/reference/datamodel.html

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

  1. Using [NumPy][numpy] as [an interface to Intel's MKL SIMD][intel_mkl]
  2. [PyPy][pypy]'s JIT compilation [achieves faster-than-C performance][pypy_c]
  3. [Disqus][disqus] scales from [250 to 500 million users on the same 100 boxes][disqus_scale]

Admittedly these are not the newest examples, just my favorites, but
it would be easy to devote a whole post to high-performance Python and
the unique offerings of various Python runtimes, but if there is one
point to be made it is to emphasize the impact of developer
productivity on end-product performance.

Given enough time, a disciplined developer can execute the only proven
approach to achieving accurate and performant software:

  1. Engineer for correct behavior, including the development of respective tests
  2. Profile and measure performance, identifying bottlenecks
  3. Optimize, paying proper respect to the test suite and Amdahl's
  Law, and taking advantage of Python's strong roots in C.

It might sound simple, but even for seasoned engineers, this can be a
very time-consuming process. Python was designed from the ground up
with developer timelines in mind. In our experience, it's not uncommon
for Python projects to undergo three or more iterations in the time it
C++ and Java to do just one.

[pypy]: http://pypy.org/
[pypy_c]: http://morepypy.blogspot.com/2011/08/pypy-is-faster-than-c-again-string.html
[disqus]: https://disqus.com/
[disqus_scale]: http://www.slideshare.net/zeeg/pycon-2011-scaling-disqus-7251315
[intel_mkl]: https://software.intel.com/en-us/articles/numpyscipy-with-intel-mkl

## Myth #5: Python does not scale

Scale has many definitions, but by any definition, YouTube is a web
site at scale. More than 1 billion unique visitors per month, over 100
hours of uploaded video per minute, and 20% of peak Internet
bandwidth, all with Python as a core technology. Dropbox, Disqus,
Eventbrite, Twilio, Instagram, EVE Online, Second Life, and, yes, eBay
and PayPal all have Python scaling stories that prove scale is more
than just possible: it's a pattern.

The key to success is simplicity and consistency. CPython, the primary
Python virtual machine, maximizes these characteristics, which in turn
makes for a very predictable runtime. One would be hard pressed to
find Python programmers concerned about garbage collection pauses or
application startup time. With strong platform and networking support,
Python naturally lends itself to smart horizontal scalability, as
manifested in systems like [BitTorrent][bittorrent].

Additionally, scaling is all about measurement and iteration. Python
is built with profiling and optimization in mind. See Myth #4 for more
details on how to vertically scale Python.

[bittorrent]: http://bittorrent.cvs.sourceforge.net/viewvc/bittorrent/BitTorrent/

## Myth #6: Python is a new language

What with all the startups using it and kids learning it these days,
it's easy to see how this myth still persists. Python is actually 23
years old, originally released in 1991, 4 years before Java. A
now-famous early usage of Python was in 1996: [Google's first
successful web crawler][google_crawler].

If you're curious about the long history of Python, Guido van Rossum,
Python's creator, [has taken the care to tell the whole
story][python_history].

[python_history]: http://python-history.blogspot.com/2009/01/introduction-and-overview.html
[google_crawler]: https://news.ycombinator.com/item?id=8587697

## Myth #7: Python is not for big projects

Myth #5 discussed Python at scale, but there is another aspect to
scaling worth discussing: people. While Instagram reached hundreds of
millions of hits a day at the time of Facebook's billion dollar
purchase, the whole company was [still only a group of a dozen or so
people][instagram]. Dropbox in 2011 [only had 70
engineers][dropbox_lean], and other teams were similarly lean. So, can
Python scale to large teams?

You better believe it. Bank of America actually has over 2,000 Python
developers. Same goes for YouTube. Big products and big teams use
Python every day. Python has excellent modularity and packaging
characteristics, but beyond a certain point, much of the general
development scaling advice stays the same: tooling, strong
conventions, and code review are what make big projects a manageable
reality.

Luckily, Python starts with a good baseline on those fronts as
well. We use [PyFlakes][pyflakes] and [other tools][flake8]to perform
static analysis of Python code before it gets checked in, as well as
adhering to PEP8, Python's language-wide base style guide.

Finally, it should be noted that, in addition to the scheduling
speedups mentioned in Myth #4 and #5, projects using Python generally
require fewer developers, as well. Our most common success story
starts with a Java or C++ project slated to take a team of 3-5
developers somewhere between 2-6 *months*, and ends with a single
motivated developer completing the project in 2-6 weeks. It's not
unheard of for some projects to take hours instead of weeks, as well.

A miracle for some, but a fact of modern development, and often a
necessity for a competitive business.

[dropbox_lean]: http://www.forbes.com/sites/victoriabarret/2011/10/18/dropbox-the-inside-story-of-techs-hottest-startup/
[pyflakes]: https://github.com/pyflakes/pyflakes/
[flake8]: https://pypi.python.org/pypi/flake8

## Myth #8: Python is not secure

Python's lightweight nature may not make it seem formidable, but the
intuition here can be misleading. One central tenet of security is to
present as small a target as possible, and CPython achieves this by
being a very simple and easily-auditable virtual machine. In fact, a
recent analysis by Coverity Software [resulted in CPython receiving
their highest quality rating][coverity_python].

Python also has an extensive array of open-source, industry-standard
security libraries. At PayPal, where we take security and trust very
seriously, we find that a combination of [PyOpenSSL][pyopenssl],
[PyCrypto][pycrypto], and [hashlib][hashlib] cover all of PayPal's
diverse security and performance needs.

For these reasons and more, Python has seen some of its fastest
adoption among the application security team here at PayPal (and eBay
for that matter). Here are just a few security-based applications
utilizing Python here in PayPal's security-first environment:

  * Creating security agents for facilitating key rotation and consolidating cryptographic implementations
  * Integrating with industry-leading HSM technologies
  * Constructing TLS-secured wrapper proxies for less-compliant stacks
  * Generating keys and certificates for our internal mutual-authentication schemes
  * Developing active vulnerability scanners

Not to mention the myriad operations-oriented systems with security
implications, such as firewall and connection management. In the
future we'll definitely try to put together a deep dive on PayPal
Python security particulars.

[coverity_python]: http://www.coverity.com/press-releases/coverity-finds-python-sets-new-level-of-quality-for-open-source-software/
[pyopenssl]: https://github.com/pyca/pyopenssl
[pycrypto]: https://github.com/dlitz/pycrypto
[hashlib]: https://docs.python.org/2/library/hashlib.html

## Myth #9: Python programmers are scarce

There is some truth to this myth. There are not as many Python web
developers as PHP or Java web developers. This is probably mostly due
to a combined interaction of industry demand and education, though
[trends in education suggest that this may change][python_education].

That said, Python developers are far from scarce. There are millions
worldwide, as evidenced by the dozens of Python conferences, tens of
thousands of StackOverflow questions, and companies like YouTube, Bank
of America, and LucasArts/Dreamworks employing Python developers by
the hundreds and thousands. At eBay and PayPal we have over 200 developers who
use Python on a regular basis, so what's the trick?

Well, why scavenge when one can create? Python is exceptionally easy
to learn, and is a first programming language [for
children][python_kids], [university students][python_university], and
[professionals][python_google_class] alike. At eBay, it only takes one
week to show real results for a new Python programmer, and they often
really start to shine as quickly as 2-3 months, all made possible by
the Internet's rich cache of interactive tutorials, books,
documentation, and open-source codebases.

Another important factor to consider is that projects using Python
simply do not require as many developers as other projects. As
mentioned in Myth #7, lean, effective teams like Instagram are a
common trope in Python projects, and this has certainly been our
experience at eBay and PayPal.

[python_education]: http://cacm.acm.org/blogs/blog-cacm/176450-python-is-now-the-most-popular-introductory-teaching-language-at-top-us-universities/fulltext
[python_university]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/
[python_kids]: http://www.nostarch.com/pythonforkids
[python_google_class]: https://developers.google.com/edu/python/?csw=1

## What to do with nine ex-myths

Mythology can be a fun pastime. Discussions around these nine myths
