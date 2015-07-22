# On names

Naming is hard. Hard enough to be one of the two remaining hard
problems in computer science, as the saying goes. That might be a bit
much, but in the long run, naming can make or break a codebase, and in
the short run, good naming conventions are vital to coding flow. In
meatspace, like in cyberspace, nothing is faster than a memory lookup,
and nothing packs memory more efficiently than a well-designed
mindhash.

## Values

First things first, this isn't some creative writing post. There are
at least two types of naming, one that's creative, like naming a
project or a child, and the second, more mechanical, routine variant,
which is reserved for naming interfaces, variables, and APIs. There
are techniques for both, but the former will have to wait.

Now, desirable characteristics to maximize in variable names:

1. Accurate
2. Meaningful
3. Short*
4. Pronounceable

<small>\* Especially when naming member variables that will necessarily be
   paired with an owning object (e.g., `myobject.member_var`).</small>

## Key conventions

1. Method names should start with a verb, especially when the
   `get_*()` pattern is applicable, where `*` describes the return
   value. This enables rule #2. Avoid verbs which commonly double as
   nouns and adjectives, e.g., `empty_*`.
2. When referring to a value that'll be returned, use `ret`. The
   nature of the value in `ret` is implied by the name of the
   method. The prevailing patterns here involve the construction of an
   empty mutable object that will be populated, or the setting of a
   default.
3. When referring to service requests, responses, and connections, standardize
   on `req`, `resp`, and `conn`. `res` or `results` is a good name
   for any data loaded from a successful response
   (e.g., `res = json.loads(resp.text)`).
   A quick aside: when `resp` is returned, it's acceptable if not
   preferred to `return resp` instead of using the `ret` naming
   convention.
4. Avoid plurals when a more container-descriptive name is
   available. For instance, `conns` implies the iterable nature of the
   value, but `conn_list`, `conn_set`, and `conn_map` resolve a lot
   more ambiguity, at a cost of 3-4 characters. I've found this to be
   most true in function and module scopes, but for member variables
   where there's only one representation of that iterable present, a
   plural often looks and sounds better.
5. When transcribing an algorithm from a paper, try hard to keep the
   variable names the same as the pseudocode, even if they break other
   naming conventions. (and don't forget to link to the paper in a
   comment).
6. Use initialisms liberally:
     * For everyday variables: `ei_list = [i for i in int_list if not i % 2]`
     * As a shortening technique for certain frequently-called
     functions or types: `from operator import itemgetter as IG`
     * For exception instances: `except ValueError as ve:`

## Even more conventions

- `ctx` is a common abbreviation for `context`, same goes for
  `mgr`/`manager`, but this style of abbreviation should never
  be used for class names and virtually never be used for
  module-level constants.
- `i` and `j` are only variable name choices when there are 1-2
  counters in a relatively short function.
- `_` is only valid in the most local of scopes. Avoid using it for
  escaping functions (use `esc`)
- Any single-letter variable name should be local (or
  closure/nonlocal-level, at most), definitely not for globals or
  members. List comprehensions are a good place for single-character
  names, where the first letter of the iterable's name is a natural
  choice (e.g., `[c for c in conn_list if c.is_secure]`).
- Avoid any variable consisting solely of repeated characters (`ii`, `jj`)
- Prefer `_map` over `_dict` (it's shorter, looks better, and sounds
  better, too)
- Never conflict with builtins* (or keywords, of course). Oblique strategies:

  * `class` -> `cls` (`klass` looks dumb, stop that. see more notes below.)
  * `type` -> `*_type` (see note below)

- Reserve `cls` for the first argument to `classmethod`s. Use `*_type`
  (e.g., `var_type`) when possible. It's better to think in terms of
  types than classes anyways.

<small>\* possible exceptions: `format`, `next`, `input`, `raw_input`</small>

## Fundamentals

These should go without saying, but just to be explicit:

* Use `ALL_CAPS` for module-level constants, `TitleCase` for classes,
  `lower_case` for variables
* `_underscore_prefix` for internal/private module or type members, as
  well as freely inside of function scopes where it aids clarity
  (generally used to indicate "technical detail" or "intermediary
  value")
* Numbers in variable names are inexcusable. Even though this makes
  names like `result1` unlikely, watch out for the trailing `l`
  (but names like `level` are fine)
* Avoid `__name_mangling` in all but the most specific cases
