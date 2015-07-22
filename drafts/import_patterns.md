# Python Import Patterns

## Relative Imports

### Implicit Relative Imports

Pros:

Cons:

* Import shadowing

### Explicit Relative Imports

Pros:

Cons:

* Can't run code from within the package. (TODO: phrasing)

## Absolute Imports

Pros:

Cons:

* Breaks if package is included in and imported from a larger
  package. In other words, `from mypackage import myfunc` breaks if
  the directory containing mypackage has its own __init__.py. Instead,
  the package will be under something like lib.mypackage. Even if
  mypackage is on sys.path, it'll still be called lib.mypackage.
