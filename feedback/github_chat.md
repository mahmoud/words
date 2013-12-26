# GitHub Design Interview

*Chrissie, Keavy, Mahmoud; Monday, December 9th, 2013*

## Likes

Generally, GitHub is a very solid and usable product, so most
everything is well-liked unless otherwise mentioned. Here are some
particular events I appreciated since I started using Github in
2008-2009.

* Code graphs (proved very useful for acquisition due diligence)
* Cloneable wiki
* Contribution graph
* Language/Trending pages (e.g., https://github.com/languages/python)
* On-site semi-rich editor (super useful for docs)
* Search for users by location (see note below though)

## Dislikes

* Separate Gist - I miss having Gists in public timelines and activity streams
* Gravatar - It's sort of OK but not great for public
  GitHub. Especially questionable for Github Enterprise.

## Other areas for improvement

* Linking from within rendered docs (Markdown, ReST docs within the codebase)
* Various minor artifacts of public Github within Enterprise ("Search 1M repositories!")
* Better default tags in Issues
* Contribution graph colorization scale, while technically
  self-consistent, not as clear as it could be (dark green is 2
  commits for some, 200 for others)
* Longstanding minor issue, repo activity graphs on the Repositories
  page take a refresh (or two) to load
* Super general thing, it'd be super cool if pages were somehow fluid
  down to 700px or so, which enables side-by-side in more screen
  sizes. My corporate laptop is 1600 across, with a vertical start
  bar, so there are about 760 horizontal pixels to work with.
* Pulse works for very large and active projects, but better surfacing
  of more basic stats (like the sort of stuff one might get out of
  CLOC) would probably work better for basic stats
* When searching for users by location, not too many people seem to
  show up. 96 Python programmers in San Jose, and I know a dozen of
  them in real life. Too many recruiters? Probably a cultural thing.

## Features

* Better usage of live activity stream (filterable by activity type,
  language, user) to surface active coders
* Better cohort discovery via technology, location, skill level,
  friend-of-friend
* More customization of what information should be surfaced on the profile page
  * Maybe more semantic fields, similar to location, for Twitter account, etc.?
* I know some teams can benefit from adding feature support (e.g.,
  graphs) for groups of repos (the Node infrastructure team at PayPal
  has dozens and dozens, for better or worse).
* Being able to tag/reference other projects, like @mentioned, but
  %project somesuch. Basically what I'd like to achieve is
  being able to call out relationships like "for use with" or
  "requires" or "compare to" other projects on Github. "inspired by"? :P
* Project analytics. For Enterprise at least.
* Make documentation even easier to write. You can never make
  documentation too easy to write. I don't know how to do this, at
  all. readthedocs.org is cool, and Sphinx is ok, but it's still not
  easy enough for me. I might just be a wuss.
* I could see some sort of "Uses this" feature, but the space might
  already be a bit tight between star/watch/fork.
* **Table of Contents in the Github-flavored Markdown**. One of the main
  reasons we use ReStructured Text instead of markdown is because of
  the Table of Contents (and overall slightly better linking).
* The ability to "star" snippets (maybe save them to a gist,
  preserving origin information?), similar to pull quotes
  (Tumblr/Kindle/etc.). Can be useful for highlighting techniques,
  especially across codebases.

## Personal musings

* I've sometimes wondered if anyone has a streak as long/longer than mine.
* I think it'd be cool to discover projects with interesting
  properties like, "lots of stars/watchers/commits, but no commits in
  the last two years," such as simplegeo's oauth2 library or akdubya's
  dustjs. "Seeking maintainer" There are probably too many interesting
  combos to list here, though.
* I've also wondered about per-user git usage styles, like stats
  surround commit sizes, for instance. Might want to be careful about
  going to deep down the quantified-self rabbithole. It can lead to
  bad optimization for some and alienation of others. Maybe best if
  these stats aren't front and center.
* Do prolific tweeters have better git commit messages? and other fun
  ways to promote better commit messages.

## Links

* Live activity stuff: rcmap.hatnote.com, listen.hatnote.com, choir.io
* Gist leveraging: bl.ocks.org (and others like dabbble that are more involved)
