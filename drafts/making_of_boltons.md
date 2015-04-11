# The Making of Boltons

Just jotting down a few thoughts in the direct aftermath, before they
get painted nostalgic:

## Technical

One explicit technical goal was many functionalities grouped together
by a consistent quality and factor (lightweight, well-described), such
that extensive cross-pollination of knowledge across subject matters
could occur in the docs. Someone looking for a cache might learn a
technique or two about debugging or statistics.

Python 3 compatibility is a headache and between Ashes and Boltons, I
think I've written enough infrastructural Python 3 to know. Everywhere
I look I still see signs that Python 3 does not add to the success of
a Python project. Many of the core libraries that were updated for 3
were long before superseded by fundamentally superior third party
libraries. Python 3's `ssl` is nice, but `PyOpenSSL` and
`cryptography` are nicer. Optimistically, Tulip shows
promise. Realistically, Twisted and greenlet-based libraries show
large-scale results. On the flip side, fundamental data types that
made Python 2 robust, have been hamstringed, making Python 3
sickly. Look no further than the `bytes` type. Bytes are the lifeblood
of computing, and the Python 3 `bytes` type is at once half-baked and
overcooked. Slicing returns strings, indexing returns numbers. The
constructor has four signatures and `bytes(2**33)` raises a
MemoryError. I'll probably write about this more elsewhere, but
several comments on boltons indicated wishes for a Python 2.8, an
opinion I'm beginning to come around to.

Several boltons are nicer than the standard library. `iterutils` are
generally more intuitive and full-featured than `itertools`. Same with
`OrderedMultiDict` vs `OrderedDict`.

Learned a lot about Sphinx. Should probably enable more social media
buttons on the Sphinx landing pages.

## Process

Boltons was a thing I remember telling people about at PyCon
2013. Over two years later, it was in a shape that carried
interest. Whether or not it could have been done sooner is moot.
I'm tired! I got woken up too early by notifications, and I had pull
requests for breakfast. The theory was to release before PyCon, since
so many people were in transit, it would be a low-supply, high-demand
time for Python news. Maybe boltons makes a good conversation topic
and I'm present by proxy of my library. Maybe it gets forgotten
because talks are awesome and people like conference atmospheres. Mark
seems a bit bitter that he didn't get pepperbox in time, but we'll get
it out soon. Boltons took forever, too.

1,500 stars in 28 hours gets you 15-20 followers and a lot of mostly
playful flak from friends.
