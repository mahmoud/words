# Rediscovering Wikipedia through Python

## Category

Python Libraries

## Duration

30 minutes, but expandable to 45 (as detailed below)

## Description

> Current shortform: Wikipedia is more than an encyclopedia, it's a giant, ever-expanding database of knowledge made freely available for people and programs alike! Python is the ideal language for capturing the subtleties of an API as nuanced as Wikipedia's. From policies to patterns and examples, come learn just how easy Python makes it to tap into and explore the sum of all human knowledge.

Wikipedia is a pillar of the modern Internet and, with hundreds of
thousands of editors, is one of largest collaborative texts ever
created. 500 million monthly users know that it is a vast source of
facts, statistics, and media about an ever-increasing number of topics
(24+ million articles) in an ever- more-complete set of languages (242
active languages, 8 languages with 1+ million articles). Articles
represent only a fraction of the content that is available on Wikipedia:
each article includes a full revision history, metadata, links, media,
categories, and more.

All of this data is freely available for re-use under a Creative Commons
license. What's often overlooked is that it also has the most open and
unrestrictive API of any site in its class.

Python is the ideal language for capturing the nuances of Wikipedia's
API, and this talk will demonstrate just how easy it can be to tap into
the sum of all human knowledge. From introduction to policies to
patterns and examples, learn all about the capabilities of the
encyclopedia written by Pythonists like you.

## Audience

> Current shortform: Wikipedia users and community members, Open data enthusiasts, API (and API design) afficionados

- Open Data enthusiasts (researchers, re-users)
- Wikipedia users and community members
- API and API design aficionados

## Python Level

Beginner to Intermediate

## Objectives

By the end of the talk, attendees should feel confident in their ability
to access Wikipedia's data through the API and live feed. They will be
knowledgeable about the data available through the Wikipedia API, Python
tools to retrieve Wikipedia data, and a few examples of how this data
can be used. They will also be introduced to considerations in designing
and using a high profile API.

## Detailed Abstract

The fifth most-trafficked website in the world, Wikipedia is a fantastic
resource for the curious Internet-goer. Wikipedia includes over 24
million articles (including a full revision history, metadata, links,
categories, media and more) accross 242 languages. Nearly all of this
data is freely accessible through the API, and much activity is
available in a real-time feed.

### Why Wikipedia?

In addition to its popularity, Wikipedia is also notably non-profit, and
relies on not just monetary contributions from supporters, but it is
composed entirely of user-generated content and powered by open-source
software contributions from capable engineers.

From the other perspective, many engineers and aspiring coders have
turned to Wikipedia to learn their craft, but may not have thought of
Wikipedia as also being a programmatically-accessible open data store
that welcomes and encourages derivative works.

### Why Python?

Wikipedia actually has a fairly decent Python community, revolving
around PyWikipediaBot-based automation. These efforts tend to revolve
more around editing and management than data and research.

The truth is that Wikipedia's API is large, inconsistent, and at times
cryptic. The technical aspects of this talk revolve around Python's
expressiveness as a solution to wrangling a normally very-involved API.

### A new Wikipedia API client: Wapiti

Over the past couple years, I have worked on several Wikipedia projects
(examples below), all of which contributed to the development of a new
API client. While the talk isn't intended to focus on implementation
specifics (unless organizers deem a 45-minute slot suitable), the
defining characteristics are:

- Focus on query-related operations (Wikipedia as a data source)
- Built for developers of all skill levels
- Ease of extensibility
- Consistent data model with exceptionally close parallels to
  Wikipedia's API

In addition to an introduction to the raw API, attendees will learn how
Wapiti makes it very easy to create and recombine API implementations to
create new ones that suit their uses, business or personal (with
examples).

### Wikipedia live feed

Also relevant for Python programmers is the ability to subscribe to
real-time Wikipedia edits as a service, developed in Python, which
enabled the construction of:

- Listen to Wikipedia (<http://listen.hatnote.com/> released August,
  2013)
- Hatnote Recent Changes Map (<http://rcmap.hatnote.com/> released
  May, 2013)

These will be demoed (or video shown) in the presentation. (Stability
isn't a major concern, feed uptime is over 97% and these were already
live-demoed during keynotes at WikiMania in Hong Kong 2013.)

### In closing

The purpose of this talk is to introduce the large amount of data that
is accessible in Wikipedia using Python. A large part of proposing this
talk is in response to the popularity of the aforementioned live feed
examples, which have gotten quite a bit of media/social media attention
(links available on request). I think audiences might also just be
interested in hearing a bit about how Python made those projects
possible, and see other examples of what they can do.

## Outline

Witty section headings TBD.

1. Intro (3 min)  
    1. Who am I?
    2. What is Wikipedia?
    3. Wikipedia has an API?
2. Wikipedia API functional overview (4 min)  
    1. What can Wikipedia's API do?
    2. What's in the documentation?
    3. How did it get to be the way it is? (large, arcane)
3. Legacy options (3 min)  
    1. Raw API (\<1 min, already mostly covered above)
    2. PyWikipedia bot (1 min)
    3. Other clients (1 min)
4. Wapiti (10 min)  
    1. Usage (5 min)
    2. Implementation (3 min)
    3. Writing custom operations (2 min)
5. Live feed (4 min)
6. Contributing (6 min)  
    1. Brief exploration of possibilities (with example code) (4 min)
    2. Getting involved in the community (1 min)
    3. Finding help (1 min)

(3 + 4 + 3 + 10 + 4 + 6 = 30 minutes)

## Notes

- This is my first proposal to speak at PyCon, though I have some
  speaking experience:
    - Numerous internal tech talks at PayPal
        - PythonASF: Python ASF Client (2011)
        - Python in the Midtier (2011)
        - Python at PayPal (2012)
        - Python, Wikipedia, and Machine Learning (2012)
        - Service Rationalization with Python (2013)
    - As the main Python evangelist within PayPal, I organized "Python
      Day", which brought together \~300 people from inside and
      outside the company (including Guido and Raymond). I MC'd, gave
      a full-length talk, and did a lightning talk. Video available on
      request.
    - BoF participation at past PyCons
    - I just did an interview with French TV for Wikipedia-related
      work, if that's relevant.
- Should organizers for some reason want more Wikipedia-related
  content at PyCon, this talk can be extended to be either more
  technical, by focusing more on Wapiti's implementation, or more
  community-centric, by focusing more on contributing.
- All code available immediately at:
    - <https://github.com/mahmoud>
    - <https://github.com/hatnote>

## Internal notes

- Internet as an industrialized and commercialized wasteland. There
  are plenty of businesses, but where are all of the
  parks/schools/libraries.
- sumofallhumanknowledge.py
- sum(all(human\_knowledge))
- The serpent, the tree, and the API: Accessing Wikipedia from Python
- Alternative title: Assuming Good Faith: Fixing PHP with Python