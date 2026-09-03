# CSA Africa — website

A rebuild of [csaafrica.org](https://www.csaafrica.org/) as a static, dependency-free
site. Same organisation, same words, same photographs — rearranged into an
editorial layout with a proper design system.

---

13 pages: home, about, team, news, INUKA Mombasa, the Python workshops, one page
per workshop edition (2025, 2022, 2021, 2019, 2018), contact and a 404.

## Running it

There is no build step to install and nothing to `npm install`. Serve the folder:

```bash
python -m http.server 8000
```

Serve it rather than opening `index.html` straight off disk. From a `file://`
URL YouTube refuses to embed the alumni films — it cannot validate a referrer,
and returns player error 153. The page degrades gracefully (the posters become
plain links to YouTube), but the inline players only work over http(s).

## Rebuilding the HTML

The `.html` files are generated. Edit content in `build_data.py` or layout in
`build.py`, then:

```bash
python build.py          # requires Pillow (for intrinsic image sizes)
```

This rewrites every page plus `sitemap.xml` and `robots.txt`.

## Layout of the repo

```
index.html  about.html  team.html  news.html            generated pages
inuka-mombasa.html  workshops.html  contact.html
csa-2025.html … csa-2018.html                           one per workshop edition
404.html  sitemap.xml  robots.txt  favicon.ico

build.py            templates, page composition, the <img> helper
build_data.py       all copy, links, people, testimonials, stats

assets/css/fonts.css  @font-face for the self-hosted typefaces
assets/css/main.css design system (tokens → components, one file)
assets/fonts/       IBM Plex Serif, IBM Plex Mono, Inter (woff2)
assets/js/main.js   nav, reveal, count-up, rail, lightbox, video facade
assets/img/
  brand/            transparent logo, favicon, the "01" tile
  story/            editorial + hero photography (+ @sm narrow variants)
  gallery/          per-edition photo sets (+ thumb/ for the grid)
  team/ people/     portraits
  partners/ news/ video/
assets/video/       the homepage background film, 480p and 720p
```

## Design system

Everything derives from the existing logo — deep navy `#0F1753`, slate `#313B56`,
amber `#FB9106`, and the Africa outline filled with binary `01`.

- **Type** — IBM Plex Serif for display, Inter for UI and body, IBM Plex Mono for
  labels and metadata. Plex is a typeface built for a technology company, which is
  why it is here rather than a trend pick. Served from `assets/fonts/`, not a CDN
  — see **Typefaces** below.
- **Motif** — the logo's `01` pattern appears twice, at very low opacity: behind
  the hero and behind the impact figures. `assets/img/brand/binary-tile.svg`.
- **Colour** — paper and ink do the work; amber is an accent, never a fill. There
  are no gradients other than photographic scrims.
- **Rhythm** — sections alternate paper / stone / navy / full-bleed photograph so
  no two adjacent bands look alike.
- **Gutter** — every container is `min(100% - var(--gutter) * 2, <max>)`, with
  `--gutter: clamp(1.25rem, 5vw, 5.5rem)`. It was a flat `1.25rem`, which left
  content 20px from the edge on a 1440 laptop — effectively flush. The original
  site ran a 980px column with ~230px of air each side; this keeps the wider
  editorial measure but gives the page a margin to sit in: 71px at 1440, 50px at
  1024, 20px on a phone. The header breakpoints are derived from it, so if you
  change the gutter, re-check the numbers in the header note.

### Rails

The testimonials (14), leadership (5) and volunteers (22) are horizontal
scrollers rather than grids, so a long roster costs one screen instead of six.
Each has a control row directly above it — count on the left, arrows on the
right — and the scrollbar is styled to be seen rather than hidden, because it
is the affordance. JavaScript retires the whole control row when everything
already fits (the leadership rail on a wide screen), so there are never dead
arrows promising a swipe that does nothing.

Every card in a rail is the same height and its footer sits on the card's floor,
so the portraits line up across the row. Testimonials vary a lot in length, so
short quotes carry whitespace above the footer — that is the cost of the shared
baseline, and it is deliberate.

### The header

Home, About, Programmes, Team, Alumni Voices, News, then **Get in touch** and
**Support our work**. Contact is not a nav item — "Get in touch" goes to the
same page, so listing both was the same destination twice; the button carries
the `aria-current="page"` state on `contact.html` instead.

Breakpoints are measured rather than guessed. The row needs ~990px at its
tightest, and the gutter eats into what is left, so the drawer takes over at
1230px (121px of clear space just above it) and the links tighten between 1231
and 1400px. The JS resize guard uses the same number as the stylesheet — if you
change one, change both.

The drawer lists the same items at a smaller size than it used to, so the whole
menu fits one phone screen without scrolling, and its footer offers **Support
our work** and **Get in touch**. Volunteering is still linked from the Team and
Workshops pages and the footer.

### Alumni Voices

The primary nav carries an **Alumni Voices** entry pointing at the testimonials
section: `#testimonials` on the homepage, `index.html#testimonials` everywhere
else. It gets no `aria-current` — it is a place on a page, not a page.

The section takes `tabindex="-1"` so the jump moves keyboard focus with it, and
a `scroll-margin-top` that only clears the sticky header: the section's own top
padding supplies the breathing room, so a larger value would just push the
heading down the screen. Measured landing clearance below the header is 73px at
1440, 49px at 1180 and 27px at 390.

A sixth nav item also needed more room than five, so the mobile drawer takes
over at 1230px rather than 1080px (CSS and the JS resize guard both), and the
links tighten between 1231 and 1400px.

### The mobile homepage

At 390px the homepage ran 13854px — sixteen screens. Four of its sections are
reproduced in full elsewhere on the site, so `.wide-only` drops them below
760px (the same width at which the announce bar and the header buttons give
way):

| Hidden on a phone | Where it still lives |
| --- | --- |
| Why CSA Africa exists | `about.html` — and the hero's "Read our story" CTA |
| What makes us different | `about.html` |
| Our Python Workshops + timeline | `workshops.html` — hero CTA "Explore the workshops" |
| Past and future workshops | `workshops.html`, and each edition is its own Programmes entry |

What stays is the hero, INUKA (an announcement, not a menu section), the impact
numbers, the testimonials, the alumni films, the partners and the closing CTA:
7486px, or nine screens. Nothing above 760px changes — desktop is byte for
byte the page it was.

Two things the cut depends on:

- **The testimonials stay.** Alumni Voices in the menu points *at* them and
  they appear on no other page, so hiding them would both delete content from
  phones and leave that menu entry with nowhere to land.
- **`.band-dark + .band-dark`** gets a hairline top border below 760px. The
  founder story was the light band separating INUKA from the stats band; with
  it gone the two dark bands meet and need the join marked.

The rule is `@media screen and (...)` on purpose — printing still produces the
whole page.

The stats band is a phone fix rather than a cut: its `auto-fit` tracks want
180px, which is one column and five full rows on a 390px screen. Below 560px it
is pinned to two columns with a smaller number, taking it from 1072px to 755px.

### Partner logos

Two rows drifting in opposite directions, in the partners' own colours (they
used to be desaturated until hover). The rows sit inside the content column, not
full bleed — the page keeps one left edge from top to bottom. Each row emits its tiles four times and
travels a quarter of the track — exactly one set, because the trailing padding
matches the gap — so the loop has no seam and the row stays filled out to about
2700px. Hover or focus pauses it; `prefers-reduced-motion` stops it and the
rows fall back to a centred static wall with each partner shown once.

### The hero on short screens

The hero is content-driven, so at full spacing its call-to-action row fell below
the fold on ordinary laptops — 26px under on 1536x864, 92px on 1366x768, 118px
on 1280x720. The display type now answers to viewport *height* as well as width
(`min(7.2vw, 12vh)`), and three `max-height` bands tighten the vertical rhythm
further as the window gets shorter. The headline is deliberately the loudest
thing on the page — 106px at 1920, 97px at 1440 — so the height bands scale it
rather than let it push the rest off-screen.

"Explore the workshops" and "Read our story" are above the fold from 1920x1080
down to 1024x600, and on phones and tablets — fully visible everywhere except
1280x720, where 88% of the row shows. That is deliberate: the headline gets the
room, and the buttons only have to be reachable without scrolling. The stats rule is left
just past the edge on purpose — it is the cue that the page continues.

### The announce bar

The two separator dots pulse, about 0.55 Hz — under the three-flashes-per-second
threshold, and off under `prefers-reduced-motion`. They are the bar's only
attention cue; nothing else moves.

### The homepage film

The hero carries the same background film as the live site
(`62e46f_3ca2622f977442c5a51cece41aed507f`, 81 seconds, muted, looping), served
from `assets/video/` at 720p on wide screens and 480p below 780px.

It autoplays wherever motion is welcome. It briefly did not in Chrome: the
script also skipped autoplay when `navigator.connection` reported a 2g/3g
`effectiveType`. That API is Chromium-only and its value is an observed-latency
guess that reads "3g" on plenty of ordinary connections — so the film played in
Firefox and Safari, which have no such API, and sat paused in Chrome. Only
`saveData` is honoured now: a setting someone deliberately turned on, rather
than a measurement. A rejected `play()` also retries once on the visitor's first
interaction instead of leaving the hero stuck on the still.

It is not in the critical path. The `<video>` ships `preload="none"` with no
`src`; the poster — the film's own first frame — is a normal `<img>`, so it is
the LCP element and the site looks finished before a byte of video moves.
JavaScript attaches the source and starts playback only when motion is welcome
and the connection isn't metered (`prefers-reduced-motion`, `saveData`,
`effectiveType`); otherwise the still holds and the corner control offers the
film instead. Playback pauses off-screen and in a hidden tab.

That corner control is a WCAG 2.2.2 requirement — moving content that runs for
more than five seconds needs a stop — and doubles as the way in for anyone the
film was withheld from.

The navy scrim lightens while the film plays (`.hero.is-film`); measured against
sampled frames the headline keeps at least 5.3:1 against white throughout.

### Typefaces

The fonts live in `assets/fonts/` and are declared in `assets/css/fonts.css`.
They used to load from `fonts.googleapis.com`, which made the page render
differently depending on whether that request happened to succeed: when it
didn't, Inter and Plex fell back to Segoe UI and Georgia, and because the
headline is sized in `ch` the whole layout reflowed — about 100px of page height
and a visibly different nav. That is why the site could look one way opened from
disk and another through a local dev server.

Self-hosted, the render is byte-identical from `file://`, from a dev server, and
with the network cut off entirely. There is now no third-party request on page
load at all.

Twelve woff2 files, 290 KB, latin and latin-ext only. Inter is one variable file
per subset declared at `font-weight: 100 900` — Google serves the same file from
four weight URLs, so storing four copies would have been 400 KB of duplication.

To regenerate: fetch the `css2` stylesheet from Google with a desktop browser
user-agent, keep the `latin` and `latin-ext` `@font-face` blocks, download each
`woff2` into `assets/fonts/`, and rewrite the `src` URLs to point there.

### The tab icon

`favicon.ico` (16/32/48), `icon-192.png`, `icon-512.png` and the
`apple-touch-icon` are all cut from `logo.png` — the CSA wordmark, in its own
navy and amber, on a white tile. Nothing is redrawn or recoloured.

They show the wordmark rather than the whole lockup because the full mark —
Africa outline, binary fill and "AFRICA" beneath — turns to grey mush below
about 48px, which is every size a browser tab actually uses. The white tile
(rather than transparency) is what keeps it legible on dark tab bars too.

Regenerate them from `logo.png` if the logo ever changes; the crop box is
5.5-94.5% across and 24.5-54.5% down.

### The logo

`assets/img/brand/logo.png` / `.webp` is the original logo with its white
background removed (alpha derived per-pixel from the source JPEG and
un-premultiplied, so the navy and amber stay exactly as drawn). The artwork
itself is unchanged — nothing redrawn, recoloured or re-proportioned.

## Content

Every word, figure, quotation, name, link and photograph comes from the live
site. Copy has only been split, re-ordered, or given headings and labels so it
can be laid out. Nothing about the organisation is invented.

The editions grid lists **workshop** editions only. The live site carried a
2026 "coming soon" card, but there was no 2026 workshop — 2026's event is INUKA
Mombasa, which has its own section and page. A future announced edition goes
back into `EDITIONS` with `slug=None`.

Two corrections were made against the source while rebuilding:

- The partner logo filed as `01-standard-black-text.png` is the **University of
  St Andrews** crest, not Standard Bank.
- The team page showed one two-person photograph for both Fionnuala Johnson and
  Stephen McQuistin; each now uses that photograph's own per-person crop, taken
  from the crop coordinates the original site already defined.

## Video posters

The three alumni posters are YouTube's own `maxresdefault` frames at 1280x720.

The 2025 documentary poster is **not** a video frame. YouTube has nothing above
480x360 for that upload (no `maxresdefault`, no `hq720`), and it is a 4:3
letterboxed still with burnt-in subtitles — cropped to the 16:9 facade and shown
at 960px it was a 2x upscale of roughly 480x270, which is why it looked blurry.
It is now the full 2025 cohort photograph — the one that was the homepage hero
before the background film — re-cut from its 7008x4672 original to 1600x900.
It carries no overlay title, because the `<h2>` directly above already names the
film and repeating it only veiled the people in the picture; that facade uses
`.vfacade--plain`, a far lighter scrim than the captioned ones need.

Every poster carries an `@sm` variant and an explicit `sizes`, so a phone
downloads the small one.

## The alumni films

Each poster is a real link to the video on YouTube that JavaScript upgrades into
an inline `youtube-nocookie` player on click. That order matters: YouTube
refuses to embed into a page it cannot validate a referrer for, so opening the
`.html` files straight off disk gives **player error 153**. Served over http(s)
the inline player works; from a `file://` copy the script stands down and the
link simply opens YouTube. Either way the click reaches the video.

If you see error 153, serve the folder rather than double-clicking the file:

```bash
python -m http.server 8000
```

## Forms

The site is static, so `contact.html` and the workshop waitlist compose a
pre-filled message to `csacademyafrica@gmail.com` via `mailto:` rather than
posting anywhere. Point `data-mailto` forms at a real endpoint (Formspree,
Netlify Forms, a Wix form URL) if you want server-side submissions.

## Accessibility and performance

- Semantic landmarks, one `<h1>` per page, skip link, visible focus rings,
  keyboard-operable dropdown, drawer and lightbox (`Esc`, arrow keys).
- Every image has alt text and intrinsic `width`/`height`, so nothing shifts as
  the page loads.
- All motion is behind `prefers-reduced-motion`.
- Images are WebP, lazy-loaded below the fold, with narrow-screen `srcset`
  variants for the large ones. YouTube loads only after a click — no third-party
  script on first paint. Total CSS + JS is under 60 KB uncompressed.
- The hero film is the one heavy asset (9.5 MB / 22 MB). It is deferred, opt-out
  and never blocks paint — but it is real mobile data, so it is skipped outright
  on metered and slow connections.
