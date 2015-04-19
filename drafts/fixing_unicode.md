# Fixing Unicode in Python 2

Lost-causers take a walk, this is something that can be done.

Step 1: Allow the unicode type to take encoding as a keyword argument
even when the first positional argument is not a bytestring. This
allows cases like this to work.

```
def get_short_text(user_input, limit=8):
    return unicode(user_input, encoding='utf-8')[:limit]
```

Now in this example user_input can be a utf-8-encoded bytestring
(instance of str), decoded text (instance of unicode), or any other
object (which will be str'd or repr'd into an instance of unicode).

Basically, make unicode() more useful than str(). This will lead to
more widespread correct usage of text over bytes. Without the change
above, there is no way to reliably get text without a try/except
block, whereas bytestrings are easily churned out with fairly reliable
calls to str().


Step 2: Remove .encode() from str instances, .decode() from unicode instances.

You call .decode() on str objects to turn them into encoding-free
text. The len() of a text object is the number of characters in that
text string, but says nothing for how many bytes will be in its
encoded format.

You call .encode() on unicode objects to turn them into encoded
bytes. The len() of a str is the number of bytes in the bytestring,
but says nothing for how many characters are in the original text.

It is gravely confusing to have .encode() on an already encoded object
such as a bytestring. It is similarly confusing to have .decode()
exist for unicode objects which have no encoding applied to them. By
simply removing these extraneous methods, easily the most confusing
errors are removed from Python.

```
>>> u'Beyoncé'.decode('utf8')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.7/encodings/utf_8.py", line 16, in decode
    return codecs.utf_8_decode(input, errors, True)
UnicodeEncodeError: 'ascii' codec can't encode character u'\xe9' in position 6: ordinal not in range(128)
```

An encode error raised from a decode call. This was never acceptable
and Python 3 is not a sufficient answer why this gun was loaded and
aimed at the common developer's foot.
