# Python Myth Busting

## 1. Python is interpreted

While Python does not require a separate compiler toolchain like C++,
it is in fact compiled to bytecode, much like Java and many other
compiled languages. Further compilation steps, if any, are at the
discretion of the runtime, be it CPython, PyPy, Jython/JVM,
IronPython/CLR, or some other process virtual machine.

## 2. Python is a scripting language

Python can indeed be used for scripting, and is one of the forerunners
of the domain due to its simple syntax, cross-platform support, and
ubiquity among Linux, Macs, and other Unix machines.

In fact, Python may be one of the most flexible technologies among
general-use programming languages. To list just a few:

  1. Telephony infrastructure (Twilio)
  2. Payments systems (PayPal, Balanced Payments)
  3. Neuroscience and psychology ([citation][neuroscience])
  4. Numerical analysis and engineering
  5. Animation (LucasArts, Disney, Dreamworks)
  6. Gaming backends (Eve Online, Second Life, Battlefield)
  7. Email infrastructure (Mailman, Mailgun)
  8. Media storage and processing (YouTube, Instagram, Dropbox)
  9. Operations and systems management (Rackspace, OpenStack)
  10. Natural language processing (NLTK)
  11. Machine learning and computer vision (scikit-learn, Orange, SimpleCV)
  12. Security and penetration testing ([citation][pentest])
  13. Big Data (Disco, Hadoop support)
  14. DNS (BIND 10)

Not to mention websites and web services aplenty.

[neuroscience]: http://www.frontiersin.org/neuroinformatics/researchtopics/Python_in_neuroscience/8
[pentest]: http://dirk-loss.de/python-tools.htm

## 3. Python is weakly-typed

Python is dynamically typed, and in fact more strongly-typed than
Java. Java has a split type system for primitives and objects, with
``null`` lying in a sort of gray area. On the other hand, modern
Python has a unified strong type system. And yes, the type of ``None``
is well-specified.

## 4. Python is slow

First, a critical distinction: Python is a programming language, not a
runtime.

There are several Python implementations.

  1. **CPython** is the reference implementation, and also the most widely
     distributed and used.
  2. **Jython** is a mature implementation of Python for usage with the JVM.
  3. **IronPython** is Microsoft's Python for the Common Language Runtime, aka .NET.
  4. **PyPy** is an up-and-coming implementation of Python, with advanced
     features such as JIT compilation, incremental garbage collection,
     and more.

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

## 5. Python does not scale

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

## 6. Python is a new language

What with all the startups using it and kids learning it these days,
it's easy to see how this myth still persists. Python is actually 23
years old, originally released in 1991, 4 years before Java.

TODO: link to Guido's history
TODO: rustle up a list early big-name users

## 7. Python is not for big projects

Myth #5 discussed Python at scale, but there is another aspect to
scaling worth discussing: people. While Instagram reached hundreds of
millions of hits a day, at the time of Facebook's billion dollar
purchase, the whole company was still only a group of a dozen or so
people. Dropbox and other teams were similarly lean. So, can Python
scale to large teams?

Bank of America actually has over 2,000 Python developers, so you
better believe it buster.

8. Python is not secure
9. Python is a web-only language
10. Python programmers are scarce

Bonus: Python is not a good language, Python programmers are just good
programmers
