# Choosing The Right Versioning System for your Project
<!-- or What Your Project's Version Says About You -->

In these times of modern software development, a project can hardly be
called a project without a proper versioning scheme. From a technical
perspective, the lack of a version number is as negligent toward
clients and integrators as lack of source control is to collaborators,
and both prove equally punishing to oneself. Beyond technical reasons,
a project's version bears a huge impact on the perception of the
project. At every turn, this critical component will appear next to
the name of the project, closer and more often than the name of the
author and maintainers.

Given this magnitude, it's a wonder that versioning schemes seem to be
mostly afterthoughts and foregone conclusions. This guide seeks to
change that by introducing some options and direction for picking the
versioning scheme that is right for projects and their maintainers.

## A few collected expectations

It's almost impossible to write more software than one encounters. As
a result, we have some general expectations about version numbers.

1. Versions increase with time - Bigger is better, less would be worse
2. Versions speak to the quality of the software - Whereas a good
   project name communicates an ideal, a good project version
   communicates the progress toward that ideal
3. Versions are trackable - Continuity is a good thing. Irregular gaps
   can cause confusion
4. Versions are numeric, except when they're not - Numeric versions are
   the default, but non-numeric versions and version components
   abound.

<!-- TODO: case studies in all of the above? -->

1. Chrome came along with a fast feature release schedule and a
   versioning system to match, a versioning system that made Firefox
   appear to be left in the dust. Firefox later changed its versioning
   system.

4. Terms like "alpha" and "beta", as well as named project versions
   like those used in Linux distributions (Debian's "jessie" or Ubuntu's
   "trusty"), are well-understood in many circles.


## Semantic versioning

Semantic Versioning, or SemVer, is the go-to versioning system for
most projects these days. A quick glance at the 40 most recent updates
on the Python Package Index (PyPI) show that all but six packages
appear to have the comfortable three-part versioning scheme. Among
those packages the highest minor version was 108 and the highest
micro version was all the way up to 595. For those unfamiliar with SemVer

First thing I have to check when I see a project version is when was
it last updated, when was it last released.

The problem with calling SemVer a "specification" is that unlike the
vast majority of successful RFC specifications, there is no validator
that can determine whether a project has correctly implemented
SemVer. If a project API breaks, but the major version is not
incremented, SemVer has been violated. More often than not the version
is not retroactively changed, and that's mostly just how project life
goes. Better to embrace the realities and treat SemVer as a detailed
recommendation rather than to argue over the polarizing MUSTs and MUST
NOTs of specification language.

## Calendar versioning

If you're an earnest engineer with honest intents of creating a
project for the long run, then calendar versioning may be for you.

* d3 could have been protovis 2.0, but instead both projects exist and
  everyone's the better for it

* Calendar versioning is actually quite commonplace when you look closely. Examples:
  * Twisted
  * Windows 95/98/2000

* If your project is being used in production by you AND someone you
  don't know, the time for a non-beta major release has already been reached.


# PyPI recent 40

Highest minor: 108
Highest micro: 595
***** 4-part
* Calendar
