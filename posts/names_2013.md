# On names

* Naming is hard. OK, not really\*, but maladroit naming definitely
  impedes the flow of programming.
* Consistent naming improves code readability and maintainability.
* Brevity is key, and often only possible through good naming
  conventions.

<small>\* There are exceptions, especially in the area of directional
relationships, like "following" and "follower"</small>

## Values

Desirable characteristics to maximize in variable names:

1. Accurate
2. Meaningful
3. Short*
4. Pronounceable

<small>\* Especially when naming member variables that will necessarily be
   paired with an owning object (e.g., `myobject.member_var`).</small>

## Key conventions

1. method names should almost exclusively start with a verb, especially
   when the `get_*()` pattern is applicable, where `*` is a description of
   what is being returned. This enables rule #2.
2. When referring to a value that'll be returned, use `ret`. The
   nature of the value in `ret` is implied by the name of the
   method. The prevailing patterns here involve the construction of an
   empty mutable object that will be populated, or the setting of a
   default.
3. When referring to service requests, responses, and connections, standardize 
   on `req`, `resp`, and `conn`. A quick aside: when `resp` is returned, it's
   acceptable if not preferred to `return resp` instead of using the
   `ret` naming convention.
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

6. Use initialisms liberally. Within function scopes 
   (e.g.,  `ei_list = [x for x in int_list if not e % 2]`) and as a
   shortening technique for certain frequently-called functions or types
   (e.g., `from operator import itemgetter as IG`)

## Even more conventions

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

<small>\* possible exception: `format`</small>

## Fundamentals

These should go without saying, but just to be explicit:

* Use `ALL_CAPS` for module-level constants, `TitleCase` for classes,
  `lower_case` for variables
* `_underscore_prefix` for internal/private module or type members, as
  well as freely inside of function scopes where it aids clarity
  (generally used to indicate "technical detail" or "intermediary
  value")
* avoid `__name_mangling` in all but the most specific cases

