# Writing rock-solid web services with Python

## Category

Best practices/patterns

## Duration

45 minutes

## Description

> Current short form: As web platforms continue to grow in relevance and complexity, the demand for ever-more dependable and introspectable services follows suit. This talk draws on experiences and examples at PayPal to detail the nuances of developing robust service infrastructure, how Python rose to those challenges, and what it all means for a large enterprise.

As web platforms continue to grow in relevance, and systems grow in
complexity, the demand for ever-more dependable and introspectable
services follows suit. This talk details the development of Python as a
platform at PayPal, the world's leading online payments processor.

Topics will include a brief history of Python at PayPal, solutions
implemented by the team, and best practice recommendations for service
infrastructure developers. Technical specifics include tackling
high-concurrency, high-performance use cases while grappling with
proprietary legacy systems, and successfully transitioning from an
unreliable, opaque C++ clunker of a runtime to a robust, instrumented,
introspectable, well-oiled almost-entirely-pure-Python machine.

Featuring appearances from such technologies such as coroutines
(gevent), threads (built-in), WSGI (gunicorn), PyOpenSSL (custom
security), and many more, including the unveiling of a couple
open-source libraries that made it all possible.

## Audience

> Short form: Developers interested in high-concurrency, high-robustness, RESTful web infrastructure and how to introduce it to new Pythonists. Also PayPal voyeurs.

Developers interested in:

- What makes software robust and how to foster robustness in their
  services
- Managing high-concurrency deterministically (specifically coroutines
  with gevent)
- The design of RESTful web infrastructure
- Introducing Python to corporate developers with a wide range of
  Python experience (tending toward minimal-to-know experience)

And anyone interested in select tales of intrigue, as told from a
Pythonist's perspective, from within the walls of the black-box behemoth
payments processor otherwise known as PayPal.

## Python Level

Experienced (except for community/corporate aspects)

## Objectives

Attendees will learn about:

- Developing robust, trustworthy services by taking a
  software-infrastructure-first approach.
- General advice and specific tips on how to balance powerful features
  with the golden rule of keeping it simple (and how Python enables
  this).
- Measurement, profiling, and metadata best practices.
- The obligations of architects and infrastructure developers to their
  developer community.

## Detailed abstract

Formed in 2010, the Python Infrastructure team at PayPal has been making
steady strides towards first-class citizenship at PayPal, which, while
having Silicon Valley startup roots, has grown into a massive
multi-thousand-developer enterprise shop. The ecosystem is a complex,
multilayered, multifaceted organism, at the heart of which still lies
decade-old C++.

### Enter Python

Python actually made its first appearances early on in PayPal's history
and has existed behind the scenes providing valuable mortar to PayPal's
many parts.

However, the real opportunity for Python opened up upon the rewrite of
PayPal's internal service-oriented architecture (SOA) infrastructure.
Leveraging the new structured services, we were able to develop a Python
client that has since grown into a full service framework, with complete
support for virtually every internal PayPal system, no matter how
proprietary.

### Performance and reliability, brought to you by introspectability

PayPal's ecosystem is one of many intertwined systems, owned by many
people, in many organizations, all with different priorities. For
instance, for compliance reasons, very few PayPal developers have access
to their software in the production environment. We have several
dedicated release and operations groups.

Historically, it has been virtually impossible to navigate all the
people, processes, and even technical systems accumulated over the last
15 years, to finally release a reliable application. In almost all
cases, there are known compromises that were made and persist.

Python's rich runtime and excelllent cross-platform support have enabled
a level of introspectability that makes it possible to change all that.
Tools for profiling, measurement, security, concurrency, debugging, and
more, have enabled us to build a highly-instrumented framework for
product developers to build applications that run as deterministically
on their local environments as they do on production.

Open-source libraries we've used include greenlet, gevent, gunicorn,
requests, werkzeug, PyOpenSSL, PyCrypto, SQLAlchemy, and more. I'll be
detailing how we stuck all these together in a fashion that keeps our
infrastructure customers happy and us sane.

### Balance

Developer life isn't all about C10K Hello, World demos and ping-pong
microbenchmarks. It's important to be real about what a full-bodied,
complete application needs in a sensitive production environment. Nine
times out of ten, an experienced developer will take a deterministic,
logged, stats-collected, reloadable, notifications-enabled service that
does "enough" requests per second over a tiny while-loop of an
application doing 50,000 more. It's the Pythonic approach applied to the
application layer.

### Community

Python is growing in industry, and evangelists in large organizations
probably share a lot of the same growing pains. Python can be a hard
sell when it's taken as "just a scripting" language or "not fast
enough". I'll be sharing tips on how we tapped into the existing users
to create a grassroots movement, got the attention of upper management,
and how we delivered results in a historically traditional corporate
shop.

## Outline

1.  Intro (8 mins)
    1.  Who am I?
    2.  Who is PayPal?
    3.  History of Python at PayPal (5 mins)
2.  Python Infrastructure (26 mins)
    1.  Motivations and ecosystem (3 mins)
    2.  Service-oriented architecture at PayPal (10 mins)
    3.  Process management (5 mins)
    4.  Logging (3 mins)
    5.  Profiling (5 mins)
        1.  Traditional
        2.  Real-time and Sampling
3.  Testing (5 mins)
4.  Other considerations (7 mins)
    1.  Packaging (3 mins)
    2.  Cross-platform support (1 min)
    3.  Security (3 mins)
5.  Community management (4 mins)
    1.  Grassroots
    2.  Upward

I can shrink this to 30 minutes by simply:

- Skipping "Other considerations" (-7)
- Skipping logging (-3)
- Shortening the intro to 5 minutes (-3)
- Shortening the SOA (2.2) to 8 minutes (-2)

## Notes

* This talk is an updated form of a talk given to an audience of about 300 (including Guido van Rossum) in 2012, the video and slides of which are available upon request ("upon-request" discretion requested because it includes some internal details).

* This is my first proposal to speak at PyCon, though I have some                                         speaking experience:                                                                                       
    - Numerous eBay-internal tech talks:
        - PythonASF: Python ASF Client (2011)
        - Python in the Midtier (2011)
        - Python at PayPal (2012)
        - Python, Wikipedia, and Machine Learning (2012)
        - Service Rationalization with Python (2013)
    - As the main Python evangelist within PayPal, I organized "Python
      Day", which brought together ~300 people from inside and outside
      the company (including Guido and Raymond). I MC'd, gave a
      full-length talk, and did a lightning talk. Video available on
      request.
    - BoF participation at past PyCons
    - I just did an interview with French TV for Wikipedia-related work, 
      if that's relevant.

* Apologies for any formatting issues, I'd originally written an RST, viewable here: https://github.com/mahmoud/misc_docs/blob/master/paypal_proposal.rst