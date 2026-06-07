# Template Catalog

20 numbered task templates in `assets/examples/`, plus `00-base-scaffold.html`
for rare cases where no numbered template is close. The templates are grouped by
six use categories. Each entry: what it is, the request that should trigger it,
and its signature components.

Copy the closest numbered file and replace its content — never start blank. If a
request spans multiple shapes, pick one primary template for the overall page and
borrow specific components from secondary examples.

## Exploration — compare options before committing

**01-exploration-code-approaches.html** — *"Show me 2-3 ways to implement X with
pros/cons."* 3-column approach grid, each with a code panel + pro/con table +
metric chips, ending in a recommendation callout. Static.

**02-exploration-visual-designs.html** — *"Explore a few visual directions for
this component."* Sticky light/dark toggle, 2×2 artboard grid rendering live
variants, per-board rationale. JS theme toggle.

## Code — review, explain, document

**03-code-review-pr.html** — *"Review this PR / these changes."* PR header with
+/- stats, risk-ranked file cards with colored diffs and speech-bubble inline
comments, collapsed safe files, next-steps checklist. JS risk-map jump + highlight.

**04-code-understanding.html** — *"Explain how X flows through the codebase."*
Summary + hand-built SVG flow diagram + numbered walkthrough with file locations
and collapsible source; sidebar of key files + gotchas. JS accordion.

**05-design-system.html** — *"Document our design system / tokens."* Color swatch
grids, type scale, spacing ruler, radius/elevation cards, component gallery.
Static. (Also the visual source for `references/design-system.md`.)

**06-component-variants.html** — *"Show the variants of this component."* Sticky
control toolbar (slider/radio/checkbox) driving live design tokens across a
variant grid, with a JSX snippet preview. JS token controls + snippet swap.

## Prototyping — feel the interaction before building it

**07-prototype-animation.html** — *"Prototype/animate this micro-interaction."*
Centered animation stage, easing-swap buttons, keyframe timeline, copy-paste CSS.
JS toggles state + swaps easing var at runtime.

**08-prototype-interaction.html** — *"Prototype drag-to-reorder so we can try the
feel."* Two-col bench: draggable sidebar mock with drop indicator + a "what you're
feeling" annotation panel. Native HTML5 drag-and-drop.

## Communication — present and report

**09-slide-deck.html** — *"Make a deck I can arrow-key through."* Full-viewport
scroll-snap slides, title ornament, progress bars, SVG sparkline, inverted
decision slide, slide counter. JS keyboard nav + IntersectionObserver counter.

**11-status-report.html** — *"Weekly/sprint status report."* Stat band, highlights,
shipped-PR table, SVG bar chart, carryover panel. Static.

**12-incident-report.html** — *"Incident postmortem with timeline + root cause."*
Severity pills, dark TL;DR, vertical timeline, root-cause diff, impact table,
action-item checklist, fixed TOC. Static.

**16-implementation-plan.html** — *"Thorough tech-design/implementation plan."*
Summary strip, milestone timeline, SVG data-flow, UI mockups, key-code blocks,
severity risk table, open questions. Static.

**17-pr-writeup.html** — *"Write up this PR for reviewers."* PR meta, TL;DR,
before/after panels, collapsible file-tour with add/mod/del badges, review-focus
list, test-plan checklist, sticky TOC. Native `<details>` + anchor TOC.

## Diagrams & research — explain a system or concept

**10-svg-illustrations.html** — *"Illustrate these technical concepts as
diagrams."* Gallery of hand-built inline SVG figures (queue, retry, fan-out) with
per-figure download buttons + palette notes. JS serializes each SVG to download.

**13-flowchart-diagram.html** — *"Diagram this pipeline as a clickable flowchart."*
SVG canvas of process nodes / decision diamonds / terminals with labeled edges,
legend, sticky detail panel. JS click swaps node detail.

**14-research-feature-explainer.html** — *"Explain how feature X works, with steps
and config."* Sticky "files read" nav, TL;DR, expandable step path, tabbed code
panel, gotchas, FAQ. JS tabs + native collapsibles.

**15-research-concept-explainer.html** — *"Explain a concept like consistent
hashing interactively."* Live SVG ring demo with sliders/buttons + readout,
comparison table, sticky glossary with hover-linked terms. JS-heavy live viz.

## Custom editing UIs — throwaway tools with copy-back

These embody the "two-way interaction" idea: the human manipulates state, then
copies the result back into the next prompt. Always include a copy/export button.

**18-editor-triage-board.html** — *"Triage these tickets into buckets I can drag,
then give me markdown."* Kanban with Now/Next/Later/Cut columns, draggable cards,
live point totals, tag filters, copy-as-markdown. Full drag/drop.

**19-editor-feature-flags.html** — *"Toggle editor for my config/flags that warns
on bad deps."* Grouped flag panels with toggle switches, dependency warnings,
sticky live-diff sidebar, copy-diff / copy-JSON. JS validation + diff.

**20-editor-prompt-tuner.html** — *"Let me edit this prompt template and preview
fills across examples live."* Contenteditable template with `{{slot}}`
highlighting, live preview against sample cards, token counter, copy/reset. JS
live highlight + render.

## Starting shell

**00-base-scaffold.html** — minimal header + panels with tokens already wired. Use
only when no numbered template above is close (rare).
