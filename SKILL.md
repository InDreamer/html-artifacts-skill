---
name: html-artifacts
description: This skill should be used when producing a deliverable for a human to read, share, or interact with — specs, code reviews, status/incident reports, slide decks, diagrams, research explainers, prototypes, or small throwaway editing UIs. It generates a single self-contained HTML file using a consistent "Acme" design system instead of plain Markdown, trading Markdown's editability for higher information density, scannability, shareability, and two-way interaction.
---

# HTML Artifacts

## Why HTML over Markdown

Markdown won the small-context era because outputs were short and edited line by
line. Capable agents now produce large, reference-grade outputs that are read and
shared more than they are hand-edited. For those, HTML is the stronger format:

- **Information density** — tables, SVG, CSS layout, and interactivity in one file;
  no ASCII-art or emoji workarounds.
- **Scannability** — collapsible sections, tabs, sticky nav, and visual hierarchy
  make a 400-line artifact navigable where raw Markdown becomes a wall of text.
- **Shareability** — one `.html` file opens in any browser, no build, no deps.
- **Two-way interaction** — sliders, toggles, and live previews let a human tune
  options and copy the result back into the next prompt.

Keep using Markdown for versioned source-of-truth files and short replies. Reach
for an HTML artifact when the output is a *deliverable*: something to present,
share, navigate, or interact with.

## When to use

Use this skill when a request maps to one of these shapes. The right-hand column
names the template to copy (full triggers and components in
`references/template-catalog.md`).

| Category | Request → template |
|---|---|
| Exploration | compare code approaches → `01`; explore visual directions → `02` |
| Code | review a PR → `03`; explain how code works → `04`; document a design system → `05`; show component variants → `06` |
| Prototyping | animate a micro-interaction → `07`; prototype drag/drop feel → `08` |
| Communication | slide deck → `09`; status report → `11`; incident postmortem → `12`; implementation plan → `16`; PR write-up → `17` |
| Diagrams & research | export SVG diagrams → `10`; clickable flowchart → `13`; feature explainer → `14`; interactive concept explainer → `15` |
| Custom editing UIs | drag-to-triage board → `18`; feature-flag editor → `19`; prompt tuner → `20` |

## How to build an artifact

1. **Pick the closest template** in `assets/examples/` and copy it as the starting
   point — never start from a blank file. The 20 numbered task templates are real,
   fully-styled artifacts; match the request to one using the table above or read
   `references/template-catalog.md` for the full per-template "use-when" guide and
   component list. Use `00-base-scaffold.html` only when no numbered template is
   close.
   - If the request spans multiple shapes, choose one **primary** template for the
     page structure, then borrow specific components from secondary examples
     (for example, a flowchart from `13` plus explainer sections from `14`).
   - After copying, keep the example's interaction pattern but replace all
     placeholder copy/data with task-specific content.
2. **Apply the design system.** Every artifact must paste the tokens from
   `references/design-system.md` into its `:root` and follow its three rules
   (fixed type roles, single `--clay` accent, calm bordered surfaces). This is
   what makes independent files read as one coherent product. Read that file
   before styling anything new. Examples may include template-local variables,
   but their shared palette should use the current Acme token names from the
   design-system reference.
3. **Fill real content.** Replace placeholder copy with the actual material.
   Prefer real data from the task; only invent illustrative data when none exists,
   and label it as illustrative.
4. **Keep it self-contained.** Inline all CSS in one `<style>` and all JS in one
   `<script>`. No external fonts, CDNs, build steps, or network calls — the file
   must work offline by double-clicking it. Use the system font stacks in the tokens.
5. **Make interactivity robust.** For editor-style artifacts, wrap JS in an IIFE
   with `"use strict"`, drive a single `render()` from current control state, and
   provide a copy-back affordance (a button writing settings/output to clipboard)
   so the human can return results to the conversation.
6. **Verify before delivering.** Confirm valid HTML structure, that the file is
   genuinely standalone (no external references), and that any JS runs without
   console errors. State the file path so the user can open it.

## Product Design Mindset

1. A prototype nobody clicks is just a painting.
2. The best design system is the one nobody notices.
3. You cannot unsee a bad font pairing. Choose carefully.
4. Every pixel argues for attention. Most should lose.
5. The fastest way to finish a design is to ship it.
6. Whitespace is not empty. It is the silence between the notes.
7. If you need more than three colors, you have zero colors.
8. The user's mental model is the only spec that matters.

## Constraints

- One file, no dependencies, works offline.
- One accent color (`--clay`); add new hues only on explicit request.
- Don't fabricate data and present it as real — mark illustrative figures.
- Match an existing project's branding only if asked; otherwise use the Acme system.
