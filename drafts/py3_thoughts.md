# Thoughts on Python 3

Python 2 is an intuitive joy to use. This is in large part because it
follows the grain of programming and computers. To those of us whom
Python won over, it *feels* natural. In order to continue in that
tradition, the same rubric should be applied to Python 3.

## Unicode

The elephant in the room, the turkey on the table.

It could be argued that a jarring violation of the aforementioned
"natural computing" principle is at the very core of Python 3:
unicode-first strings. What are we assuming about the architecture of
a program when we actively empower decoded text over bytes? The one
thing we know for sure is that this program is being executed on a
computer. Computers deal in bytes. It is easy to write a useful
string-based program that only deals in bytes, and it is virtually
impossible to write a useful program that only deals in decoded
unicode text and literals. I believe much of the resistance against
Python 3 is due to the subconscious but widespread suspicion
surrounding this unnatural decision.

NB: Python 2 made mistakes with regard to unicode. The str type should
have had no .encode() member and the unicode type should have had no
.decode(). The double-encode/double-decode problem generated
immeasurable confusion and frustration surrounding the already
confusing topic of encodings and the relatively-new Unicode
systems. Rationalizing this API alone would make Python 2 infinitely
more intuitive in the area of text processing.

## The ``io`` system

XXX

## Async

The parts of Python that make it great are the parts that keep it
architecturally neutral. Between the good parts of the standard
library, one ends up hopscotching between imperative, object-oriented,
and functional programming that may sound bad in principle, but works
extremely well. The parts that see the least usage are the parts
polarized around a specific architecture.

For example, ``itertools`` is great, if you're writing a particular
type of code. The iterator style ends up becoming rather pervasive
within one's codebase and can lead to the code not feeling very
Pythonic. Strong, neutral data structures like the dict, list, tuple,
and set form the foundation of Python. A practical and powerful type
system creates the scaffolding for large, maintainable
codebases. Succinct and pithy patterns like list comprehensions make
the line-to-line code a pleasure to write.

If Python is to continue being Python, it must maintain this
neutrality and allow a thousand flowers to bloom. "There should only
be one way to do it" must only be applied up until a point. That point
is application architecture. Python does not succumb readily to
labels, and a plurality of supported architectures is the best way to
retain that nature.

Looking at demand, Greenlets belong in the standard library. Looking
at the symmetry with ``weakref``, futures belong in the standard
library.
