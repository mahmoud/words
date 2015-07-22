# Learning Your Own Library

How does software advance? Not on its own, but in steps taken by
developers, big and small. It's quite common for a step to be
particularly large, bigger than the original author.

As a result, when crafting software that creates new idioms, the
implementation may come before an exact usage pattern is known, and it
can take a while for those necessary patterns to become obvious. The
most notorious modern example of this is probably CSS. The committees
that created CSS have surprisingly little overlap with the actual
expert users, and it took many years after the release of CSS for the
patterns we take for granted to emerge. You don't ask a W3C person how
to make a responsive footer that stays at the bottom of the page on
all browsers.

Some kinds of new code just take time (and a ideally a community) to
discover how to use them. It might not even be an API problem, the API
could be fine. Sufficiently advanced APIs need time to accumulate the
idioms to make them usable.

It's not ideal, but it's reality. The code comes first, even if it's
hard to use. Without an implementation, how much trust can one ascribe
to theoretical usage prescriptions? This is what makes porting
libraries between languages so effective. Not that the approach of the
library being ported is universally applicable, just that it has more
user understanding to build on.
