# Python Myth Busting

1. Python is interpreted

While Python does not require a separate compiler toolchain like C++,
it is in fact compiled to bytecode, much like Java and many other
compiled languages. Further compilation steps, if any, are at the
discretion of the runtime, be it CPython, PyPy, Jython/JVM,
IronPython/CLR, or some other process virtual machine.

2. Python is a scripting language

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

3. Python is weakly-typed

Python is dynamically typed, and in fact more strongly-typed than
Java. Java has a split type system for primitives and objects, with
``null`` lying in a sort of gray area. On the other hand, modern
Python has a unified type system and the type of ``None`` is well
specified.

4. Python is slow

First, an important technicality: Python is a programming language,
not a runtime.

There are several Python implementations.

  1. CPython is the reference implementation, and also the most widely
     distributed and used.
  2. Jython is a mature implementation of Python for usage with the JVM.
  3. IronPython is Microsoft's Python for the Common Language Runtime, aka .NET.
  4. PyPy is an up-and-coming implementation of Python, with advanced
     features such as JIT compilation, incremental garbage collection,
     and more.


5. Python does not scale
6. Python is a new language
7. Python is not for big projects
8. Python is not secure software
9. Python is a web-only language
10. Python programmers are scarce

Bonus: Python is not a good language, Python programmers are just good
programmers
