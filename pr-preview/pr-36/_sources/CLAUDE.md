# Cross-repo context for EK125-notebooks

This file exists to carry over knowledge from work done across the wider
EK125 repo ecosystem that isn't obvious from this repo's own content. This
repo has no README.md/CONVENTIONS.md of its own the way EK125 and the
slides repos do -- treat this file as the closest thing to one for now.

## What this repo is

The instructor-side staging repo most public EK125 content gets ported
*from*. It is itself built as a second, internal-only jupyter-book site
(`_config.yml` + `_toc.yml`, `execute_notebooks: force`), separate from and
not linked to the public EK125 site.

**Do not trust this repo's content as automatically current or clean.**
Files here have repeatedly turned out to be:
- **Stale**: missing content that the actually-distributed version has
  (e.g. a coding-standards section, a time estimate), or carrying old
  grading language that predates the Fall 2026 "graded for submission
  only" policy change.
- **Polluted**: GPP files here are sometimes the *solved* version with
  worked answers baked into what should be a blank student scaffold (e.g.
  `gpp/Class_1_GPP.ipynb` is literally EK125WIP's S26 "Class 1
  Morning.ipynb" retitled, including joke placeholder names like "Josh
  Semeter/Joe Schmoe/Amelia Bedelia" baked into the intro text -- not just
  in the solutions file, in the supposedly-blank GPP itself).

Before porting anything from here to a public repo, cross-check against
what students are actually currently given (a real downloaded/distributed
copy), the same way you'd audit any other source.

## Gitignored private content, never to be published

- `/HWs/` -- real homework files including solutions (e.g.
  `Homework_4_SOLUTIONS.ipynb`).
- `/ipp/` -- real Individual Practice Problem files including solutions
  (e.g. `Class 5 IPP SOLUTION.docx`). Note: this is a *different*
  provenance from the public `EK1225-IPP` repo's decks (which were built
  from PDFs in that repo's own `docs/` folder) -- don't assume the two
  overlap 1:1.

Both are excluded from this repo's own `_toc.yml` and gitignored. Never
copy content out of either into any public repo without stripping
solutions and re-verifying it's meant to be public at all.

## Build health

A full `jb build .` here currently succeeds but with a large number of
warnings (~285 as of this writing) -- most of it is noise from `.venv/`
being scanned as content (a Sphinx `exclude_patterns` gap, not a content
problem) plus some unrelated template/transition warnings. This repo has
no "N-warning baseline" convention the way the public EK125 site does; a
high warning count here isn't itself a red flag, but a genuine
`CellExecutionError` would be -- check for that specifically if a build
here looks wrong. (An earlier GPP-solutions-backfill session left Classes
1, 3, 4, 5, and 6's Solutions notebooks in a broken, mid-repair state at
one point -- as of this writing that's resolved; all five execute cleanly.
If you find execution errors in this repo's `gpp/*_Solutions.ipynb` files
again, it may be a regression worth flagging.)

## Upstream source: EK125WIP

`EK125WIP` (`briandepasquale/EK125WIP`, personal, not under the BU-EK125
org) is the actual raw-material repo one level further upstream. GPP
solutions here were minted from files there. It's organized by semester
(`S26`, `F25`, `F26`, `copyOfShared`) rather than by class at the top
level -- see `EK125WIP`'s own `CLAUDE.md` for its structure in detail.

## Known open items worth checking before assuming fixed

- **Classes 14 and 15's GPPs were found misaligned with their own readings
  by one class** (Class 14's GPP actually covers Class 13's material --
  scope, argument-passing, copying). Not confirmed fixed.
- The term **"IPP"** (Individual Practice Problem, contrasted with GPP =
  Group Practice Problem) appears to have replaced Class 1's old GPP
  entirely in the S26 semester materials -- if you're ever asked to work
  on "Class 1's GPP" for a future semester, check whether it's been
  superseded by an IPP instead.
- A pedagogical sequencing critique was raised for Classes 1-4 (Act 1):
  `input()`/type-casting aren't formally taught until Class 4 even though
  Class 3 uses them; Class 4 opens by calling itself a "wrap-up" catch-up
  class. Not acted on -- a design question for the instructor, not
  something to unilaterally restructure.

## Site-structure convention

GPP vs. reading pages are distinguished in the sidebar nav purely by
toctree nesting depth (`toctree-l1` = reading, `toctree-l2` = GPP), not by
filename pattern -- documented in a comment at the top of this repo's own
`_static/custom.css`, if present.

## The wider ecosystem

See `EK125`'s own `CLAUDE.md` for the full repo map (EK1225-IPP,
EK125-C1-DePasquale-Slides, EK125-hw-help, EK125-discussions,
EK125-Instructors), the Act 1/2/3 course structure, and the PII-stripping
rule that applies to anything sourced from here.
