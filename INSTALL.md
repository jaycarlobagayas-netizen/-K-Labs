# BPED Research Section Update — Install Guide

Three changes to `index.html`. All CSS variables and class names already exist in your
site, so the new blocks inherit the maroon/gold theme automatically.

---

## 1. Leadership change (2 edits)

### 1a. Org chart — replace the Chairperson card

**FIND** (one line, near the end of the Organizational Structure section):

```html
<div class="org-card lead" role="listitem"><div class="org-ava" aria-hidden="true">JB</div><h3>Jay Carlo S. Bagayas, MSPE</h3><p class="org-role">Chairperson, Bachelor of Physical Education</p></div>
```

**REPLACE WITH:**

```html
<div class="org-card lead" role="listitem"><div class="org-ava" aria-hidden="true">JW</div><h3>Jessel Gay Wacan, MSPE</h3><p class="org-role">Chairperson, Bachelor of Physical Education</p></div>
```

### 1b. Faculty list — swap Wacan out, Bagayas in

**FIND:**

```html
<li>Jessel Gay Wacan, MSPE</li>
```

**REPLACE WITH:**

```html
<li>Jay Carlo S. Bagayas, MSPE</li>
```

(Wacan moves up to the Chairperson card; Bagayas takes her slot in the faculty grid,
keeping the list at 15 names.)

---

## 2. Add the analytics styles

Open `research-analytics.css`. Copy its entire contents and paste them at the **end of
the existing `<style>` block** in `index.html` — immediately before `</style>`.

---

## 3. Replace the publications section

**FIND** the whole block that begins:

```html
<!-- PUBLICATIONS -->
<section class="section" id="publications" aria-labelledby="h-pubs">
```

…and ends at the matching `</section>` (just before `<!-- FACEBOOK UPDATES -->`).

**DELETE** that entire block and **PASTE** the full contents of `research-section.html`
in its place.

Then paste the contents of `research-analytics.js` inside a new `<script>` tag placed
just before `</body>`:

```html
<script>
  /* ...contents of research-analytics.js... */
</script>
```

---

## What you get

- **KPI row** — 20 publications, 9 Scopus-indexed, 7 years represented, 5 Scholar profiles
- **Donut chart** — Scopus (9, 45%) vs Non-Scopus (11, 55%), animated on scroll
- **Bar + trend chart** — publications per year, 2010 → 2026
- **Google Scholar cards** — all five faculty profiles, opening in a new tab
- **Filter buttons** — All / Scopus / Non-Scopus over the publication grid
- **20 publication cards** — the original 6 plus 14 newly added from the Scholar profiles

No external libraries. The charts are hand-drawn inline SVG, so the page keeps working
offline and adds zero network requests.

---

## ⚠️ Verify before publishing

Scopus indexing was inferred from journal reputation, **not** checked against the live
Scopus source list. Please confirm these before going public — flip the `"scopus"` flag in
`pubs.json` and re-run `python3 gen.py` if any are wrong:

| Publication | Journal | Marked |
|---|---|---|
| 6-Week Target Tactics Training Program (2026) | Kinesiologia Slovenica | Scopus |
| Active Lives, Fulfilled Needs (2025) | Sportis | Scopus |
| Filipino Teachers' Favorable Experiences (2024) | The Physical Educator | Scopus |
| Phenomenological Probe (2023) | Sportis | Scopus |
| The Contribution of Participation (2025) | Journal of Physical Education | Non-Scopus |
| Valuing Inclusive Recreational Activities (2023) | Kepes | Non-Scopus |

**Excluded on purpose:** Sammielyn Lavente's Scholar profile lists a single article
(Montagnino et al., *PM&R*, on orthobiologic therapies) that is not her work. Her profile
is linked in the Scholar cards, but that paper is not in the repository or the analytics.
Once the profile is corrected, add her papers to `pubs.json` and regenerate.

**Also excluded:** two duplicate Poblador entries that appear twice on Google Scholar
(a title-only stub of the 2024 *Physical Educator* paper, and a fragment of the 2022
*Edu Sportivo* paper).

---

## Regenerating

`pubs.json` is the single source of truth. Edit it, then:

```bash
python3 gen.py
```

This rewrites `research-section.html`, `research-analytics.css`, and
`research-analytics.js` with updated counts, charts, and cards.
