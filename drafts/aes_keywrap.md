# AES Keywrap notes

With AES keywrap, every block affects every other block, whereas
chaining only earlier blocks affect later blocks. Signal processing
calls this "noncausal" - the "future" can affect the "past".

## Pros

* Uses the same IV (initialization vector) every time, so it's a nicer
  API basically.
* User doesn't have to have separate IV field tracked alongside the ciphertext
* Also means don't need to guarantee IV uniqueness (if IVs aren't
  unique, almost every mode has some degree of vulnerability, CTR
  (counter) especially)
* Because the IV is included with the plaintext before wrapping, it
  acts like a MAC/integrity check.
* No nonce (salt?) necessary
* Has padding scheme built in so the user doesn't need to do that either.

## Cons

* Ciphertext is bigger than plaintext (by 8-15 bytes)
* More expensive
* No streaming
* Limited to 4 GB


All in all AES keywrap should probably only be used for keys. It has a
new mode for working with ciphertext less than 8 bytes, but what keys
have less than 8 bytes?
