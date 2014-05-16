# Wikimedia as a platform

One of the biggest tech announcements of the decade dropped not two
months ago and, even if you saw it, you probably missed it. Every tech
journalist and innovator, like ships in the night.

Wikimedia wikis added OAuth.

Still doesn't seem like a big deal? When one of the biggest websites
in the world offers free hosting, free infrastructure, a free
platform, it's a big deal. Wikipedia's storage and bandwidth,
combined with a powerful user system, comprises a formidable platform.

Wikipedia is a Wikimedia-run wiki. Last I checked, Wikipedia was the
5th most trafficked website in the world. Bigger than Amazon, bigger
than eBay, bigger than Twitter. Way bigger than Soundcloud, Vimeo, or
Flickr.

## Building on Commons

What if you could build Soundcloud, Vimeo, or Flickr, but not have to
worry about hosting or bandwidth? Let alone reliability. (Do you
remember the last time Wikipedia was down?)

Wikimedia Commons exists solely to provide warehousing of reusable
media, and has been doing so for Wikipedia for many years now.

## The technicals

Now, I'm an engineer, and I'm sure some of you are, too. Savvy ones,
too, I bet. So here are some technical counterarguments for those
intent on being gift horse dental hygienists:

### API integration

Mediawiki's API is expansive and powerful. It can be quirky, but for
anyone who has spent some time on the road of taking significant
traffic on AWS (or any other IaaS or PaaS), its complexity probably
won't even register on the scale.

If you're working in PHP or Python, there's a bevy of API work already
done for you. Hatnote has basic implementations of [Mediawiki OAuth]
and [basic write operations], but you can also check out
[pywikipediabot] for some more involved write operations.

### Licensing

* Most people going to SoundCloud/Vimeo/Flickr probably prefer CC
  licenses, don't know about them, or would be fine with virtually any
  license.
* Service to content creators, helping them understand and choose good
  licenses
* Obvious benefits to content consumers (and society)

Plus the synergies of providing more media content that is usable on
Wikipedia and other Wikimedia wikis.
