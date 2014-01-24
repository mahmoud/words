# On documentation

Last night, Jared Zimmerman, Director of User Experience for the
Wikimedia Foundation, solicited for "the most human-readable
documentation" ever seen. There are some beautiful examples out there,
but one would be remiss to not delve deeper into what makes
documentation effective and excellent.

* Docs need to conform to the API, you can't layer someone else's good docs on your API
* You'd be surprised the ways that docs can "fix" an API

* Docs have always been aimed at human-readability. Machine readable
  docs are still (slowly) making their inroads (e.g., Google
  Discovery), but don't hold your breath.

* Human readability is inherently qualitative and subjective. If we
  were talking about machine readability, we'd have a shot at
  comparing apples to apples.

* Like any form of human communication/design, it starts with
  analyzing the audience. Who is the audience for the API? What are
  your platform's developers like?

* The question changes. We can be more specific than "human". Which
  services have the best docs - for their API?

* Twitter may have great API docs, but the last thing I'd want to see
  is Twitter-like docs for Mediawiki's APIs. Mediawiki's APIs are
  expansive and involved in ways that Twitter simply isn't.

* I've always found PHP docs conform excellently to the expectations
  of the budding PHP user.  Python docs quickly grow on the avid
  Python user, as well. (Counterexamples: Java, and worse, C++, which
  practically require books)

# Recipe for good docs

## The basics

* Should have a prose Getting Started component with an example
  suitable to each platform targeted (e.g., Mac has curl, Linux has
  wget)
* Should have a section for clients/drivers
* Should have prose tutorial spotlights for involved tasks (e.g.,
  Python Socket HOWTO)

## For your reference

* Must have a reference component that is precise, uniform, and easy
  to parse. This section should be automatically generated from code
  to guarantee API-documentation parallelism.
* Each API should have several working examples (yes, documentation
  should have tests, at least for testing broken links).
* Ideally, there should be a reverse index linking reference sections
  back to any referencing prose sections (such as the Getting Started
  section). This maximizes access/exposure to examples.


## Entities

Getting serious now. Most very basic services are of an RPC type,
"remote procedure call". Actions. Verbs. Many newer, more polished
APIs are based on resources. Entities. Nouns.

Good services run the gamut, and purity is neither here nor
there. (self-consistency > purity) It doesn't matter if a service is
more entity-oriented or action-oriented, there are always a mix of
both. It is absolutely critical that both get sufficient
treatment.

The biggest, most common mistake in documenting big, powerful APIs is
to document individual operations, without overarching descriptions of
the implicit entities involved across actions. Prose sections
describing the relationships of entities between each other, as well
as their respective actions are the "missing manual" for virtually every
API out there.

Concretely, for MediaWiki, what is a Page? What's the difference
between an Article and a Page? What is a Revision? What is the
difference between a Revision and a RecentChange? How are Namespaces
formmed? These are entities referred to by countless operations in the
MediaWiki API, but aside from a loose correlation with the database
schema, there's never any overall taxonomy defined.

The clearer, more consistent the definitions of these entities, the
more the API lends itself to easy, intuitive learning, hence teaching,
thus documentation. Things will click and "just work" and so forth.

APIs lacking clearly defined, consistent entities will have present a
major challenge to creating successful documentation. At the same
time, while APIs can't change, documentation can. If documentation
calls out these implicit entities, clearly connecting the dots, it can
actually heal a "broken" API.

(Oh yeah, PS, accuracy. Inaccuracy or out-of-dateness is the ultimate
betrayal a document can perpetrate on its project. It saps developer
trust and confidence in the whole project, not just the document.)
