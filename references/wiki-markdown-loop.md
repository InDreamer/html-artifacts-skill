# Wiki And Markdown Loop

Use this reference when generating HTML for a local-first wiki, Obsidian vault, project memory, worklog, handoff, decision log, `AGENTS.md`, or `CLAUDE.md`.

## Principle

Markdown remains the durable source of truth. HTML is a temporary review, visualization, editor, or export surface.

Use Markdown for:

- durable facts and claims
- source links
- decisions and tradeoffs
- worklogs and handoffs
- wiki pages future agents should search

Use HTML for:

- comparing options
- reviewing dense state
- visualizing dependencies or timelines
- triaging or editing structured items
- exporting a clean Markdown patch or focused prompt

## Workflow

1. Read the smallest relevant Markdown source set.
2. Preserve source authority:
   - latest user instruction
   - repo/vault rules
   - current index/dashboard/decision log
   - worklogs and MOCs
   - older notes
3. Generate one focused HTML artifact for a concrete job.
4. Include export controls for the next durable action.
5. Name the Markdown target for any write-back.
6. After execution, update Markdown or present a patch if the target is unclear.

## Output Location

For wiki-like repositories:

- Default to `<workspace>/.agent-html/`.
- Do not write generated HTML into `wiki/` by default.
- Do not write generated HTML into `raw/` unless the artifact itself is being preserved as source evidence.
- If a generated artifact becomes durable evidence, add explicit metadata and source/provenance before preserving it.

## Export Formats

Useful exports:

- `Copy Worklog Entry`
- `Copy Decision Entry`
- `Copy Wiki Patch`
- `Copy Handoff`
- `Copy Single Task Prompt`
- `Copy Selected Tasks`
- `Copy Markdown Summary`

Preserve:

- wiki links such as `[[Project MOC]]`
- Markdown links
- tags
- task checkboxes
- heading hierarchy
- status/TODO markers

## Anti-Patterns

- Treating the HTML board as the only place where project truth lives.
- Exporting one huge multi-agent prompt instead of scoped prompts.
- Losing source links when exporting back to Markdown.
- Mixing fact, interpretation, and speculation without labels.
- Creating a beautiful dashboard with no write-back path.
