# The "Acme" Design System

Every artifact shares one visual language so a set of separate files reads as one
product. Copy these tokens verbatim into the `<style>` block of every artifact.

## Design tokens (paste into `:root`)

```css
:root {
  /* palette */
  --ivory:  #FAF9F5;  /* page background */
  --paper:  #FFFFFF;  /* panels, cards */
  --slate:  #141413;  /* primary text */
  --clay:   #D97757;  /* single accent — links, active state, key bars */
  --clay-d: #B85C3E;  /* accent hover/pressed */
  --oat:    #E3DACC;  /* warm fill, secondary surfaces */
  --olive:  #788C5D;  /* success / positive only */
  --g100:   #F0EEE6;  /* hairline dividers, code bg */
  --g200:   #E6E3DA;
  --g300:   #D1CFC5;  /* borders */
  --g500:   #87867F;  /* muted / caption text */
  --g700:   #3D3D3A;  /* secondary text */

  /* type */
  --serif: ui-serif, Georgia, "Times New Roman", Times, serif;
  --sans:  system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --mono:  ui-monospace, "SF Mono", Menlo, Monaco, Consolas, monospace;

  /* shape */
  --radius-panel: 12px;
  --radius-row:   8px;
  --border: 1.5px solid var(--g300);
}
```

## The three rules that make it cohere

1. **Type roles are fixed.** Serif (weight 500, `letter-spacing: -0.01em`) for all
   headings and display numbers. Sans for body. Mono — uppercase, 11px,
   `letter-spacing: 0.08em`, color `--g500` — for eyebrows, labels, and metadata
   only. Never mix these roles.
2. **One accent.** `--clay` is the *only* saturated color in normal use. `--olive`
   appears only for genuine success states. Everything else is ivory/paper/slate
   plus grays. Resist adding colors.
3. **Calm surfaces.** Background `--ivory`, panels `--paper` with `--border` and
   `--radius-panel`. No drop shadows by default — separation comes from the border
   and the warm background contrast. Generous padding (panels ~24px, page ~48px).

## Baseline body + layout

```css
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: var(--ivory);
  color: var(--slate);
  font-family: var(--sans);
  font-size: 15px;
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
}
.wrap { max-width: 1120px; margin: 0 auto; padding: 48px 32px 96px; }
```

## Common component recipes

**Eyebrow label** (kicker above a heading):
```css
.eyebrow {
  font-family: var(--mono); font-size: 12px; letter-spacing: 0.12em;
  text-transform: uppercase; color: var(--g500);
  display: flex; align-items: center; gap: 12px;
}
.eyebrow::before { content:""; width:24px; height:1.5px; background:var(--clay); }
```

**Panel / card:** `background: var(--paper); border: var(--border);
border-radius: var(--radius-panel); padding: 24px;`

**Pill / tag:** mono 11px, `padding: 2px 8px; border-radius: 999px;
background: var(--g100); color: var(--g700);`

**Accent button:** `background: var(--clay); color: var(--paper); border: none;
border-radius: var(--radius-row); padding: 8px 16px; font-weight: 500;` —
hover swaps to `--clay-d`.
