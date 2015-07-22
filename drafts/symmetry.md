# Symmetry in code

Symmetry is aesthetically pleasing. Nothing quite complements itself
like itself. Symmetry has a functional side, too. Symmetrical entities
are easier to teach. The versatility of the "vice-versa" shorthand.

Python is a wonderful language, but there are several places where it
lacks symmetry. Here are just a few:

  * The `traceback` module formats and outputs stack traces, but
    cannot parse the stack traces it outputs.
  * The `weakref` module provides simple but highly-functional support
    for objects that exist now and may go away. A similarly simple
    `futures` module based on the weakref API would be a very useful
    concurrency primitive: objects that are not realized yet, but will
    be in the future.
  *
