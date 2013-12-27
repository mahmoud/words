# On names

* Naming is hard. OK, not really\*, but maladroit naming definitely
  impedes the flow of programming.
* Consistent naming improves code readability and maintainability.
* Brevity is key, and often only possible through good naming
  conventions.

\* There are exceptions, especially in the area of directional
relationships, like "following" and "follower"

Desirable characteristics to maximize in variable names:

1. Accurate
2. Meaningful
3. Short*
4. Pronounceable

\* Especially when naming member variables that will necessarily be
   paired with an owning object (e.g., `myobject.member_var`).

1. method names should almost exclusively start with a verb, especially
   when the `get_*()` pattern is applicable, where `*` is a description of
   what is being returned. This enables rule #2.

2. `ret` should be used when naming the value to be returned. The
   prevailing pattern here involves the construction of an empty
   mutable object that will be populated. The nature of `ret` is
   implied by the name of the method.

3. `req` and `resp` are vital abbreviations for constructing various
   service requests and responses. When `resp` is returned, it's
   acceptable if not preferred to `return resp` instead of using the
   `ret` naming convention.

4. Avoid plurals when a more container-descriptive name is
   available. For instance, `connections` implies the iterable nature
   of the value, but `connection_list`, `connection_set`, and
   `connection_map` resolve a lot more ambiguity.

5. When transcribing an algorithm from a paper, try hard to keep the
   variable names the same as the pseudocode, even if they break other
   naming conventions. (and don't forget to link to the paper in a
   comment).

- `ctx` is a common abbreviation for `context`
- `i` and `j` are only variable name choices when there are 1-2
  counters in a relatively short function.
- `_` is only valid in the most local of scopes. Avoid using it for
  escaping functions (use `esc`)
- Any single-letter variable name should be local (or
  closure/nonlocal-level, at most), definitely not for globals or
  members.
- Avoid any variable consisting solely of repeated characters (`ii`, `jj`)
- Prefer `_map` over `_dict` (it's shorter, looks better, and sounds
  better, too)
- Never conflict with builtins* (or keywords, of course). Alternatives:

  * class -> cls (klass looks dumb, stop that. see more notes below.)
  * type -> *_type (see note below)

- Reserve `cls` for the first argument to `classmethod`s. Use `*_type`
  (e.g., `var_type`) when possible. It's better to think in terms of
  types than classes anyways.

\* possible exception: `format`
