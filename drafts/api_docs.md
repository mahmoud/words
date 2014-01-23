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
