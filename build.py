# -*- coding: utf-8 -*-
"""
Static site generator for csaafrica.org.

Run:  python build.py
Output: plain HTML files in the repository root — no server, no framework.
Content lives in build_data.py; layout and design live here.
"""
import os
import html as H
from PIL import Image

import build_data as D

ROOT = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(ROOT, "assets", "img")
SITE = "https://www.csaafrica.org"

_dims = {}


def dims(rel):
    """Intrinsic size of an asset, so every <img> can reserve its space."""
    if rel not in _dims:
        with Image.open(os.path.join(IMG, rel + ".webp")) as im:
            _dims[rel] = im.size
    return _dims[rel]


def img(rel, alt, cls="", eager=False, style="", sizes="(min-width: 900px) 50vw, 100vw"):
    """<img> with intrinsic size, and a narrow-screen source where one exists."""
    w, h = dims(rel)
    srcset = ""
    if os.path.exists(os.path.join(IMG, rel + "@sm.webp")):
        sw = dims(rel + "@sm")[0]
        srcset = (' srcset="assets/img/{r}@sm.webp {sw}w, assets/img/{r}.webp {w}w" sizes="{s}"'
                  .format(r=rel, sw=sw, w=w, s=sizes))
    return (
        '<img src="assets/img/{rel}.webp"{srcset} width="{w}" height="{h}" alt="{alt}"{cls}{style} '
        '{load}>'.format(
            rel=rel, srcset=srcset, w=w, h=h, alt=H.escape(alt, quote=True),
            cls=' class="%s"' % cls if cls else "",
            style=' style="%s"' % style if style else "",
            load='loading="eager" fetchpriority="high" decoding="async"' if eager
                 else 'loading="lazy" decoding="async"',
        )
    )


def esc(s):
    return H.escape(s, quote=False)


ARW = '<span class="arw" aria-hidden="true">&#8594;</span>'
CHEV = ('<svg width="11" height="11" viewBox="0 0 12 12" aria-hidden="true">'
        '<path d="M2 4.5L6 8.5l4-4" stroke="currentColor" stroke-width="1.5" fill="none" '
        'stroke-linecap="round"/></svg>')
LI_ICON = ('<svg width="13" height="13" viewBox="0 0 24 24" aria-hidden="true" fill="currentColor">'
           '<path d="M4.98 3.5C4.98 4.88 3.87 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1 4.98 2.12 4.98 3.5z'
           'M.22 8.02h4.56V24H.22V8.02zM8.34 8.02h4.37v2.18h.06c.61-1.15 2.1-2.37 4.32-2.37 4.62 0 '
           '5.47 3.04 5.47 6.99V24h-4.56v-7.28c0-1.74-.03-3.98-2.43-3.98-2.43 0-2.8 1.9-2.8 3.86V24'
           'H8.34V8.02z"/></svg>')

EDITION_NAV = [(e["year"], e["slug"], e["place"]) for e in D.EDITIONS if e["slug"]]


# ------------------------------------------------------------------ chrome
def filesize(rel):
    """Human-readable size of a file in the repo, measured at build time so the
    label can never drift from the file it describes."""
    n = os.path.getsize(os.path.join(ROOT, rel))
    return "%.1f MB" % (n / 1048576.0) if n >= 1048576 else "%d KB" % round(n / 1024.0)


def rail_controls(what, cls=""):
    """Prev/next arrows for a [data-rail]. Must live inside the rail's
    [data-rail-wrap] or main.js will not find them."""
    arrow = ('<svg width="15" height="15" viewBox="0 0 16 16" aria-hidden="true">'
             '<path d="M{d}" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>')
    return (
        '<div class="rail-controls{c}" data-reveal>'
        '<button class="rail-btn" type="button" data-rail-prev aria-label="Previous {w}">{l}</button>'
        '<button class="rail-btn" type="button" data-rail-next aria-label="More {w}">{r}</button>'
        '</div>'.format(w=what, c=(" " + cls) if cls else "",
                        l=arrow.format(d="10 2L4 8l6 6"), r=arrow.format(d="6 2l6 6-6 6"))
    )


def announce():
    """The promo strip that used to sit above the header. Not rendered: one
    navy strip above the nav is enough, and the topbar has that slot now.

    Kept because a future call for applications is the case it exists for.
    To bring it back, past-tense the copy below and restore {announce}
    between {topbar} and {header} in page()."""
    return (
        '<div class="announce"><div class="shell--wide"><div class="announce__in">'
        '<span><b>INUKA Mombasa</b></span><span class="dot"></span>'
        '<span class="hide-sm">10&#8211;13 September &#183; Swahilipot Hub, Mombasa</span>'
        '<span class="dot hide-sm"></span>'
        '<a href="inuka-mombasa.html">Read about the programme &#8594;</a>'
        '</div></div></div>'
    )


def header(active):
    def link(href, label, key):
        cur = ' aria-current="page"' if key == active else ""
        return '<a href="%s"%s>%s</a>' % (href, cur, label)

    editions = "".join(
        '<a href="%s.html">CSA %s <em>%s</em></a>' % (s, y, p.split(",")[0])
        for y, s, p in EDITION_NAV
    )
    prog_open = ' aria-current="page"' if active in ("workshops", "inuka") or active.startswith("csa-") else ""

    # The testimonials live on the homepage, so this is a same-page jump there
    # and a cross-page one everywhere else. No aria-current: it is a place on a
    # page, not a page.
    voices_href = "#testimonials" if active == "home" else "index.html#testimonials"

    return """<header class="site-header">
<div class="shell--wide"><div class="site-header__in">
  <a class="brand" href="index.html" aria-label="{org} — home">
    <img src="assets/img/brand/logo.webp" width="40" height="42" alt="" fetchpriority="high">
    <span class="brand__txt">Computer Science<span>Academy Africa</span></span>
  </a>

  <nav class="nav" aria-label="Primary">
    {home}
    {about}
    <div class="nav__group">
      <button class="nav__toggle" type="button" aria-expanded="false"{prog_open}>Programmes {chev}</button>
      <div class="nav__menu">
        <a href="inuka-mombasa.html">INUKA Mombasa <em>Sept 2026 &#183; Recap</em></a>
        <a href="workshops.html">Python Workshops <em>Annual</em></a>
        {editions}
      </div>
    </div>
    {team}
    {voices}
    {news}
  </nav>

  <div class="header-cta">
    <a class="btn btn--ghost" href="contact.html"{contact_cur}>Get in touch</a>
    <a class="btn btn--amber" href="{donate}" target="_blank" rel="noopener">Support our work</a>
    <button class="burger" type="button" aria-expanded="false" aria-controls="drawer" aria-label="Open menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</div></div>
</header>

<div class="drawer" id="drawer" aria-hidden="true">
  <div class="shell">
    <nav class="drawer__nav" aria-label="Mobile">
      <a href="index.html">Home</a>
      <a href="about.html">About</a>
      <a href="inuka-mombasa.html">INUKA Mombasa</a>
      <details class="drawer__sub">
        <summary>Python Workshops {chev}</summary>
        <ul>
          <li><a href="workshops.html">Overview <em>How we work</em></a></li>
          {drawer_editions}
        </ul>
      </details>
      <a href="team.html">Team</a>
      <a href="{voices_href}">Alumni Voices</a>
      <a href="news.html">News</a>
    </nav>
    <div class="drawer__foot">
      <a class="btn btn--amber" href="{donate}" target="_blank" rel="noopener">Support our work</a>
      <a class="btn btn--ghost" href="contact.html"{contact_cur}>Get in touch</a>
    </div>
    <p class="drawer__meta">Get in touch: <a href="mailto:{email}">{email}</a></p>
  </div>
</div>""".format(
        org=D.ORG,
        chev=CHEV,
        prog_open=prog_open,
        editions=editions,
        drawer_editions="".join(
            '<li><a href="%s.html">CSA %s <em>%s</em></a></li>' % (s, y, p.split(",")[0])
            for y, s, p in EDITION_NAV),
        home=link("index.html", "Home", "home"),
        about=link("about.html", "About", "about"),
        team=link("team.html", "Team", "team"),
        voices='<a href="%s">Alumni Voices</a>' % voices_href,
        voices_href=voices_href,
        news=link("news.html", "News", "news"),
        contact_cur=' aria-current="page"' if active == "contact" else "",
        donate=D.LINKS["donate"],
        volunteer=D.LINKS["volunteer"],
        email=D.EMAIL,
    )


def socials_html():
    return "".join(
        '<a href="%s" target="_blank" rel="noopener" aria-label="%s on %s">'
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="%s"/></svg></a>'
        % (url, D.ORG, name, path)
        for name, url, path in D.SOCIALS
    )


def topbar():
    """Social links above the header, site-wide. The only strip up there.

    Deliberately not sticky: .site-header is, and a second strip riding down
    the screen would eat the thumb zone for links you follow once."""
    return ('<div class="topbar"><div class="shell--wide"><div class="topbar__in">'
            '<span class="topbar__tag">Follow CSA Africa</span>'
            '<div class="socials socials--sm">%s</div>'
            '</div></div></div>' % socials_html())


def footer():
    prog = "".join('<li><a href="%s.html">CSA Africa %s</a></li>' % (s, y) for y, s, _ in EDITION_NAV)
    return """<footer class="site-footer">
<div class="shell--wide">
  <div class="footer-grid">
    <div>
      <div class="footer-brand">
        <img src="assets/img/brand/logo.webp" width="56" height="59" alt="CSA Africa logo" loading="lazy">
        <div><strong>Computer Science<br>Academy Africa</strong></div>
      </div>
      <p class="footer-about">{about}</p>
      <a class="footer-mail" href="mailto:{email}">{email}</a>
    </div>

    <div class="footer-col">
      <h4>Explore</h4>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="team.html">Team</a></li>
        <li><a href="news.html">News</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </div>

    <div class="footer-col">
      <h4>Programmes</h4>
      <ul>
        <li><a href="inuka-mombasa.html">INUKA Mombasa</a></li>
        <li><a href="workshops.html">Python Workshops</a></li>
        {prog}
      </ul>
    </div>

    <div class="footer-col">
      <h4>Get involved</h4>
      <ul>
        <li><a href="{volunteer}" target="_blank" rel="noopener">Apply as volunteer</a></li>
        <li><a href="contact.html">Partner with us</a></li>
        <li><a href="{donate}" target="_blank" rel="noopener">Make a donation</a></li>
      </ul>
      <div class="socials" style="margin-top:1.4rem">{socials}</div>
    </div>
  </div>

  <div class="footer-base">
    <span>&#169; <span data-year>2026</span> {org}. All Rights Reserved.</span>
    <span class="mono">School of Computing Science &#183; University of Glasgow</span>
  </div>
</div>
</footer>""".format(
        about=esc(D.FOOTER_ABOUT), email=D.EMAIL, prog=prog,
        volunteer=D.LINKS["volunteer"], donate=D.LINKS["donate"],
        socials=socials_html(), org=D.ORG,
    )


def page(filename, title, description, body, active, og_image="story/csa2025-group"):
    doc = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{site}/{fn}">
<meta name="theme-color" content="#0f1753">

<meta property="og:type" content="website">
<meta property="og:site_name" content="{org}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{site}/{fn}">
<meta property="og:image" content="{site}/assets/img/{og}.webp">
<meta name="twitter:card" content="summary_large_image">

<link rel="icon" href="favicon.ico" sizes="32x32">
<link rel="icon" href="assets/img/brand/icon-192.png" type="image/png" sizes="192x192">
<link rel="icon" href="assets/img/brand/icon-512.png" type="image/png" sizes="512x512">
<link rel="apple-touch-icon" href="assets/img/brand/apple-touch-icon.png">

<link rel="preload" href="assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/ibm-plex-serif-400-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/fonts.css">
<link rel="stylesheet" href="assets/css/main.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
{topbar}
{header}
<main id="main">
{body}
</main>
{footer}
<script src="assets/js/main.js" defer></script>
</body>
</html>
""".format(
        title=H.escape(title, quote=True), desc=H.escape(description, quote=True),
        site=SITE, fn=filename, org=D.ORG, og=og_image,
        topbar=topbar(),
        header=header(active), body=body, footer=footer(),
    )
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(doc)
    return filename


# ------------------------------------------------------------------ blocks
def cta_band():
    return """<section class="cta-band">
  <div class="cta-band__media">{media}</div>
  <div class="shell">
    <p class="eyebrow" data-reveal>Get involved</p>
    <h2 class="h1" data-reveal>Ready to Transform Lives?</h2>
    <p class="lead" data-reveal>Join us in empowering the next generation of African tech innovators.</p>
    <div class="btn-row" data-reveal>
      <a class="btn btn--amber" href="{volunteer}" target="_blank" rel="noopener">Apply as Volunteer {arw}</a>
      <a class="btn btn--on-dark" href="contact.html">Partner With Us {arw}</a>
      <a class="btn btn--on-dark" href="{donate}" target="_blank" rel="noopener">Make a Donation {arw}</a>
    </div>
  </div>
</section>""".format(
        media=img("story/teamwork", "CSA Africa participants working together during a workshop",
                  sizes="100vw"),
        volunteer=D.LINKS["volunteer"], donate=D.LINKS["donate"], arw=ARW)


def partner_wall(heading=True):
    """Two rows of partner logos, drifting in opposite directions.

    Each row's tiles are emitted COPIES times and the track travels 1/COPIES of
    its own width, which is exactly one set — so the loop is seamless. Four sets
    means three are always off to the right, and the row stays filled on
    displays up to roughly 2700px. The repeats are aria-hidden so a screen
    reader hears the partner list once."""
    COPIES = 4
    half = (len(D.PARTNERS) + 1) // 2
    rows = (D.PARTNERS[:half], D.PARTNERS[half:])

    def track(items, reverse):
        tiles = "".join('<div class="partner">%s</div>' % img(p, "%s logo" % name)
                        for name, p in items)
        dupe = tiles.replace('<div class="partner">', '<div class="partner" aria-hidden="true">')
        return ('<div class="marquee{r}"><div class="marquee__track">{a}{b}</div></div>'
                .format(r=" marquee--reverse" if reverse else "",
                        a=tiles, b=dupe * (COPIES - 1)))

    head = ""
    if heading:
        head = ('<div class="sec-head sec-head--split">'
                '<div data-reveal><p class="eyebrow">Our Partners</p>'
                '<h2 class="h2">Universities, funders and industry backing the work</h2></div>'
                '</div>')
    # inside the shell, so the logos start on the same left edge as every other
    # section — a full-bleed marquee broke the page's one vertical line
    return ('<section class="section--tight section">'
            '<div class="shell">{h}'
            '<div class="partner-wall" data-reveal>{a}{b}</div></div>'
            '</section>').format(h=head, a=track(rows[0], False), b=track(rows[1], True))


def testimonial_cards(items):
    out = []
    for name, cohort, photo, quote in items:
        out.append(
            '<article class="tcard"><blockquote>{q}</blockquote>'
            '<footer>{im}<div><div class="who">{n}</div>'
            '<div class="cohort">{c}</div></div></footer></article>'.format(
                q=esc(quote), im=img(photo, name), n=esc(name), c=esc(cohort)))
    return "".join(out)


def gallery_block(year, count, label):
    shots = "".join(
        '<button type="button" data-full="assets/img/gallery/csa{y}-{i:02d}.webp" '
        'aria-label="Open photo {i} of {n}"><img src="assets/img/gallery/thumb/csa{y}-{i:02d}.webp" '
        'width="{w}" height="{h}" loading="lazy" decoding="async" alt="{alt}"></button>'.format(
            y=year, i=i, n=count,
            w=dims("gallery/thumb/csa%s-%02d" % (year, i))[0],
            h=dims("gallery/thumb/csa%s-%02d" % (year, i))[1],
            alt=H.escape("%s — photograph %d" % (label, i), quote=True))
        for i in range(1, count + 1))
    return ('<div class="gallery" data-gallery>%s</div>' % shots)


def video_facade(vid, poster, label, alt=None, sizes=None, show_label=True):
    """A real link to the video, which JS upgrades into an inline player.

    The link is the ground truth: with no JavaScript, or from a file:// copy
    where YouTube refuses to embed (player error 153, no referrer to validate),
    the click still reaches the video instead of a broken frame."""
    return ('<div class="vfacade{cls}">'
            '<a class="vfacade__hit" href="https://www.youtube.com/watch?v={v}" '
            'target="_blank" rel="noopener" data-video="{v}" data-video-title="{t}" '
            'aria-label="Play: {t}">{im}'
            '<span class="vfacade__play"><svg width="20" height="22" viewBox="0 0 20 22" '
            'aria-hidden="true"><path d="M19 11L0 22V0z" fill="currentColor"/></svg></span>'
            '{lab}</a></div>').format(
        cls="" if show_label else " vfacade--plain",
        lab='<span class="vfacade__label">%s</span>' % H.escape(label, quote=True)
            if show_label else "",
        v=vid, t=H.escape(label, quote=True),
        im=img(poster, alt or label,
               **({"sizes": sizes} if sizes else {})))


# ------------------------------------------------------------------ home
def home():
    stats = "".join(
        '<div class="stat" data-reveal><b{cnt}>{v}</b><span>{l}</span></div>'.format(
            v=v,
            cnt="" if n is None else ' data-count="%d" data-prefix="%s" data-suffix="%s"' % (n, pre, suf),
            l=esc(label))
        for v, n, pre, suf, label in D.IMPACT)

    diffs = "".join(
        '<li data-reveal><span class="n">%02d</span><p>%s</p></li>' % (i, esc(t))
        for i, t in enumerate(D.DIFFERENTIATORS, 1))

    tracks = "".join(
        '<li><div class="row"><span class="n">%02d</span><h3>%s</h3></div></li>' % (i, esc(t))
        for i, t in enumerate(D.TRACKS, 1))

    timeline = "".join(
        '<li data-reveal><span class="n">Step %02d</span><h3>%s</h3><p>%s</p></li>' % (i, esc(w), esc(d))
        for i, (w, d) in enumerate(D.TIMELINE, 1))

    editions = []
    for e in D.EDITIONS:
        if not e["slug"]:
            editions.append(
                '<article class="edition edition--soon" data-reveal>'
                '<span class="edition__tag" style="background:var(--navy);color:#fff">%s</span>'
                '<div class="edition__year">%s</div>'
                '<p class="edition__place">%s</p>'
                '<span class="edition__more">Applications open Jan / Feb</span></article>'
                % (e["tag"], e["year"], e["place"]))
        else:
            editions.append(
                '<a class="edition" href="{s}.html" data-reveal>'
                '<span class="edition__img">{im}</span>'
                '<div class="edition__year">{y}</div>'
                '<p class="edition__place">{p}<br>{d}</p>'
                '<span class="edition__more">View the edition {arw}</span></a>'.format(
                    s=e["slug"], y=e["year"], p=esc(e["place"]), d=esc(e["dates"]),
                    im=img(e["img"], "CSA Africa %s, %s" % (e["year"], e["place"])), arw=ARW))

    feature = D.TESTIMONIALS[0]
    films = "".join(
        video_facade(v, p, l, sizes="(min-width: 1100px) 31vw, (min-width: 660px) 46vw, 100vw")
        for v, p, l in D.ALUMNI_FILMS)

    body = """
<section class="hero">
  <div class="hero__media">
    {hero_img}
    <video class="hero__video" muted loop playsinline preload="none" tabindex="-1" aria-hidden="true"
           poster="assets/img/story/home-video-poster.jpg"
           data-hero-video
           data-src-sm="assets/video/csa-home-480p.mp4"
           data-src-lg="assets/video/csa-home-720p.mp4"></video>
  </div>
  <div class="hero__scrim"></div>
  <button class="hero__motion" type="button" hidden data-hero-motion aria-pressed="true">
    <span class="hero__motion-ico" aria-hidden="true"></span>
    <span data-hero-motion-label>Pause background video</span>
  </button>
  <div class="shell--wide hero__in">
    <p class="eyebrow">{org} &#183; Since 2018</p>
    <h1 class="display">Empowering young Africans with computing skills</h1>
    <p class="hero__sub">An international outreach initiative backed by the University of Glasgow,
      running intensive three-week Python programming workshops across the continent.</p>
    <div class="btn-row hero__actions">
      <a class="btn btn--amber" href="workshops.html">Explore the workshops {arw}</a>
      <a class="btn btn--on-dark" href="about.html">Read our story {arw}</a>
    </div>
    <div class="hero__stats">
      <div><b>700+</b><span>Lives transformed</span></div>
      <div><b>13</b><span>African countries</span></div>
      <div><b>50%</b><span>Female participation</span></div>
    </div>
  </div>
</section>

<!-- ---------------------------------------------------------- INUKA -->
<section class="band-dark section" style="position:relative;overflow:hidden">
  <div class="shell--wide">
    <div class="split split--wide-text" style="align-items:center">
      <div>
        <p class="eyebrow" data-reveal>September 2026 &#183; Completed</p>
        <h2 class="h1" data-reveal>INUKA Mombasa</h2>
        <p class="lead" data-reveal style="margin-top:1.25rem;max-width:48ch">
          CSA Africa&#8217;s first mindset transformation event, run with the NAA&#8217;M
          Initiative and <a class="ilink" href="{swahilipot}" target="_blank" rel="noopener">Swahilipot
          Hub Foundation</a>.</p>
        <p class="lead" data-reveal style="max-width:48ch">Four days in Mombasa, Kenya. Sixty
          places, eighteen speakers, and no coding required &#8212; only the courage to challenge
          what you believe is possible.</p>
        <ul class="detail-list" data-reveal style="margin-top:2.25rem;max-width:34rem">
          <li><span class="k">Dates</span><span class="v">{dates}</span></li>
          <li><span class="k">Venue</span><span class="v">{venue}</span></li>
        </ul>
        <div class="btn-row" data-reveal style="margin-top:2rem">
          <a class="btn btn--amber" href="inuka-mombasa.html">See what happened {arw}</a>
        </div>
      </div>
      <div class="split__media" data-reveal><div class="framed">{inuka_img}</div>
        <p class="figure-caption" style="color:var(--on-dark-2)">CSA Africa 2025 &#183; University of Nairobi</p>
      </div>
    </div>
  </div>
</section>

<!-- ---------------------------------------------------------- why -->
<section class="section wide-only">
  <div class="shell--wide">
    <div class="split split--wide-media">
      <div>
        <p class="eyebrow" data-reveal>Why CSA Africa exists</p>
        <h2 class="h2" data-reveal style="max-width:14ch">Three rejections. A decade alone.
          Two weeks that changed everything.</h2>
        <div class="prose" data-reveal style="margin-top:1.75rem">
          <p>After failing three times to break into computer science, our founder
            (<a class="ilink" href="{sofiat}" target="_blank" rel="noopener">Dr Sofiat
            Olaosebikan</a>) spent a decade teaching herself computing with no guidance.
            Two weeks of Python training in 2014 changed her trajectory completely.</p>
          <p>That&#8217;s why CSA Africa exists: to be that critical launchpad for every young African
            with potential.</p>
          <p>Our workshops are designed for university students, early-career researchers, and
            professionals.</p>
        </div>
        <p style="margin-top:2rem" data-reveal>
          <a class="tlink" href="about.html">Read Our Full Story {arw}</a></p>
      </div>
      <div class="split__media" data-reveal>{founder_img}
        <p class="figure-caption">Dr Sofiat Olaosebikan with CSA Africa participants</p>
      </div>
    </div>
  </div>
</section>

<!-- ---------------------------------------------------------- difference -->
<section class="section band-stone wide-only">
  <div class="shell--wide">
    <div class="sec-head sec-head--split">
      <div data-reveal>
        <p class="eyebrow">What makes us different?</p>
        <h2 class="h2">The barrier was never only the code</h2>
      </div>
      <p class="lead" data-reveal>We remove the practical and psychological obstacles that keep
        talented people out of the room &#8212; so the learning can actually land.</p>
    </div>
    <ul class="numlist numlist--2" data-reveal-group>{diffs}</ul>
  </div>
</section>

<!-- ---------------------------------------------------------- impact -->
<section class="band-dark section stats-band">
  <div class="stats-band__binary" aria-hidden="true"></div>
  <div class="shell--wide">
    <div class="sec-head sec-head--split">
      <div data-reveal>
        <p class="eyebrow">Our impact in numbers</p>
        <h2 class="h2">Eight years, five workshops, one continent</h2>
      </div>
    </div>
    <div class="stats-grid" data-reveal-group>{stats}</div>
  </div>
</section>

<!-- ---------------------------------------------------------- workshops -->
<section class="section wide-only">
  <div class="shell--wide">
    <div class="split split--flip">
      <div>
        <p class="eyebrow" data-reveal>Our Python Workshops</p>
        <h2 class="h2" data-reveal style="max-width:16ch">Three weeks that rewrite what people
          believe they can build</h2>
        <p class="lead" data-reveal style="margin-top:1.5rem">We run our annual workshops in
          collaboration with host universities across Africa. We&#8217;ve partnered with institutions
          in Nigeria, Rwanda, and Kenya, with plans to expand further across the continent.</p>
        <p data-reveal style="margin-top:1.5rem;color:var(--ink-2)">Our workshops are intensive and
          hands-on with multiple tracks catering to different experience levels:</p>
        <ul class="tracks" data-reveal style="margin-top:1.25rem">{tracks}</ul>
        <p style="margin-top:2rem" data-reveal>
          <a class="tlink" href="workshops.html">How the workshops work {arw}</a></p>
      </div>
      <div class="split__media" data-reveal>{workshop_img}
        <p class="figure-caption">Hands-on session &#183; CSA Africa 2025</p>
      </div>
    </div>

    <div style="margin-top:clamp(3rem,6vw,5rem)">
      <p class="eyebrow" data-reveal>Application timeline</p>
      <ul class="timeline" data-reveal-group>{timeline}</ul>
    </div>
  </div>
</section>

<!-- ---------------------------------------------------------- editions -->
<section class="section band-stone wide-only">
  <div class="shell--wide">
    <div class="sec-head sec-head--split">
      <div data-reveal>
        <p class="eyebrow">Past and future workshops</p>
        <h2 class="h2">Every edition, in its own place</h2>
      </div>
      <p class="lead" data-reveal>Ibadan, Kigali, online through the pandemic, Lagos,
        Nairobi &#8212; five cohorts since 2018.</p>
    </div>
    <div class="card-grid card-grid--editions" data-reveal-group>{editions}</div>
  </div>
</section>

<!-- ---------------------------------------------------------- testimonials -->
<section class="section" id="testimonials" tabindex="-1"
         aria-labelledby="testimonials-h" data-rail-wrap>
  <div class="shell--wide">
    <div class="sec-head sec-head--split">
      <div data-reveal>
        <p class="eyebrow">Our testimonials</p>
        <h2 class="h2" id="testimonials-h">What changed, in their words</h2>
      </div>
      <p class="lead" data-reveal>Fourteen participants, in their own words &#8212; on what the
        three weeks changed for them.</p>
    </div>

    <div class="quote-feature" data-reveal>
      <div class="quote-feature__portrait">{feat_img}</div>
      <div>
        <blockquote class="pullquote">&#8220;{feat_quote}&#8221;
          <cite>{feat_name} &#183; {feat_cohort}</cite>
        </blockquote>
      </div>
    </div>
  </div>

  <div class="shell--wide" style="margin-top:clamp(2.5rem,5vw,4rem)">
    <div class="rail-head" data-reveal>
      <p class="num">{nquotes} more<span class="rail-hint"> &#183; swipe or use the arrows</span></p>
      {tcontrols}
    </div>
    <div class="rail rail--quotes" data-rail tabindex="0" role="group"
         aria-label="Participant testimonials, scrollable">{cards}</div>
  </div>
</section>

<!-- ---------------------------------------------------------- films -->
<section class="section band-dark">
  <div class="shell--wide">
    <div class="sec-head sec-head--split">
      <div data-reveal>
        <p class="eyebrow">Alumni Success Stories</p>
        <h2 class="h2">Hear it from them</h2>
      </div>
    </div>
    <div class="video-grid" data-reveal-group>{films}</div>
  </div>
</section>

{partners}
{cta}
""".format(
        hero_img=img("story/home-video-poster",
                     "A CSA Africa t-shirt printed with the words: Empowering young Africans with computing skills",
                     cls="hero__poster", eager=True, sizes="100vw"),
        org=D.ORG, arw=ARW,
        swahilipot=D.LINKS["swahilipot"],
        dates=D.INUKA["dates"], venue=esc(D.INUKA["venue"]),
        inuka_img=img("story/session", "A CSA Africa session in progress at the 2025 workshop"),
        sofiat=D.LINKS["sofiat_gla"],
        founder_img=img("story/founder-story",
                        "Dr Sofiat Olaosebikan with CSA Africa participants"),
        diffs=diffs, stats=stats, tracks=tracks, timeline=timeline,
        workshop_img=img("story/workshops", "A hands-on coding session at a CSA Africa workshop"),
        editions="".join(editions),
        feat_img=img(feature[2], feature[0]),
        feat_quote=esc(feature[3]), feat_name=esc(feature[0]), feat_cohort=esc(feature[1]),
        cards=testimonial_cards(D.TESTIMONIALS[1:]),
        tcontrols=rail_controls("testimonials"),
        nquotes=len(D.TESTIMONIALS) - 1,
        films=films,
        partners=partner_wall(),
        cta=cta_band(),
    )
    return page("index.html", "CSA Africa — Empowering young Africans with computing skills",
                "Computer Science Academy Africa runs intensive three-week Python programming "
                "workshops across the continent. 700+ lives transformed across 13 African countries.",
                body, "home")


# ------------------------------------------------------------------ about
def about():
    after = "".join('<li>%s</li>' % esc(t) for t in D.AFTER_WORKSHOP)

    body = """
<section class="phero">
  <div class="phero__media">{hero}</div>
  <div class="phero__scrim"></div>
  <div class="shell--wide">
    <p class="eyebrow">About us</p>
    <h1 class="h1">How CSA Africa started</h1>
    <p class="phero__sub">Founded in 2018 by Dr Sofiat Olaosebikan &#8212; but the story begins with
      three rejections and a decade of fumbling in the dark.</p>
  </div>
</section>

<section class="section">
  <div class="shell--wide">
    <div class="split split--wide-text split--top">
      <div class="prose">
        <p class="num" data-reveal>01 &#8212; The beginning</p>
        <p class="lead" data-reveal style="margin-top:1rem;color:var(--ink)">Computer Science Academy
          (CSA) Africa was founded in 2018 by Dr Sofiat Olaosebikan, but the story begins with three
          rejections and a decade of fumbling in the dark.</p>
        <div data-reveal style="margin-top:1.5rem">
          <p>Three times, Sofiat applied to study computer science. Three times, she did not secure
            admission. She pivoted to mathematics and spent ten years teaching herself programming
            alone, with no one to tell her the way.</p>
          <p>Then, in 2014, everything changed. Two weeks of Python programming at AIMS Ghana
            unlocked what years of struggling alone could not. Within two years, she earned a
            fully-funded PhD in Computing Science at the University of Glasgow and began her career
            in computing.</p>
        </div>
      </div>
      <div class="split__media" data-reveal><div class="framed">{founder}</div>
        <p class="figure-caption">Dr Sofiat Olaosebikan, Founder and Lead</p>
      </div>
    </div>
  </div>
</section>

<section class="section--tight section band-dark">
  <div class="shell--narrow" style="text-align:center">
    <blockquote class="pullquote" data-reveal>&#8220;How many brilliant young Africans are fumbling
      alone right now? How many have the same potential but lack that critical launchpad and someone
      believing in them?&#8221;
      <cite>Dr Sofiat Olaosebikan, on settling in Glasgow</cite></blockquote>
  </div>
</section>

<section class="section">
  <div class="shell--wide">
    <div class="split split--top">
      <div class="prose">
        <p class="num" data-reveal>02 &#8212; What we discovered</p>
        <h2 class="h2" data-reveal style="margin-top:1rem">Only 17% of our participants were women</h2>
        <div data-reveal style="margin-top:1.5rem">
          <p>In July 2018, CSA Africa&#8217;s first workshop brought together 100 students at the
            University of Ibadan. But the workshop revealed something unexpected. The real barriers
            weren&#8217;t just access to training or resources; they ran deeper, into confidence,
            representation, and support systems.</p>
          <p>After our first few workshops, we noticed a troubling pattern: only 17% of our
            participants were women. We discovered that the barriers weren&#8217;t about access to
            computers or internet alone; they were psychological.</p>
          <p>It was confidence. It was seeing no one who looked like them succeeding in tech. It was
            a mother choosing between attending a workshop and caring for her child. It was a
            motivated student unable to afford travel.</p>
        </div>
      </div>
      <div class="split__media" data-reveal>{discovered}
        <p class="figure-caption">CSA Africa 2025 &#183; University of Nairobi</p>
      </div>
    </div>
  </div>
</section>

<section class="section band-stone">
  <div class="shell--wide">
    <div class="sec-head sec-head--split">
      <div data-reveal>
        <p class="num">03 &#8212; What we changed</p>
        <h2 class="h2" style="margin-top:1rem">In 2022, we became intentional</h2>
      </div>
      <p class="lead" data-reveal>We stated clearly: &#8220;Women are strongly encouraged to
        apply.&#8221; We introduced childcare support. We provided accommodation and covered road
        transportation. We built mentorship into the programme structure.</p>
    </div>

    <div class="feat-grid feat-grid--4" data-reveal-group>
      <div class="feat" style="background:var(--paper-2)">
        <span class="n">BEFORE 2022</span>
        <div class="h1" style="font-family:var(--serif);color:var(--ink-3)">17%</div>
        <p style="margin-top:.5rem">Female participation</p>
      </div>
      <div class="feat" style="background:var(--navy);color:#fff">
        <span class="n" style="color:var(--amber)">SINCE 2022</span>
        <div class="h1" style="font-family:var(--serif);color:var(--amber)">50%+</div>
        <p style="margin-top:.5rem;color:var(--on-dark-2)">And it has stayed there</p>
      </div>
      <div class="feat" style="background:var(--paper-2)">
        <span class="n">WHAT FOLLOWED</span>
        <p style="margin-top:.5rem">Mothers attended with their children. Students from remote areas
          gained access.</p>
      </div>
      <div class="feat" style="background:var(--paper-2)">
        <span class="n">WHAT THEY REPORTED</span>
        <p style="margin-top:.5rem">Participants reported feeling skilled, confident, and supported.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell--wide">
    <div class="split split--flip split--top">
      <div class="prose">
        <p class="num" data-reveal>04 &#8212; Our participants</p>
        <h2 class="h2" data-reveal style="margin-top:1rem">Not only computer scientists</h2>
        <div data-reveal style="margin-top:1.5rem">
          <p>CSA Africa workshops are designed for university students, early-career researchers, and
            professionals who are eager to build their programming confidence and apply computing
            skills to their studies, research, or work.</p>
          <p>Our participants come from diverse academic backgrounds:</p>
        </div>
        <ul class="tag-row" data-reveal style="margin-top:1.25rem">
          <li class="tag">Mathematics</li><li class="tag">Engineering</li><li class="tag">Medicine</li>
          <li class="tag">Pharmacy</li><li class="tag">Nursing</li><li class="tag">Law</li>
          <li class="tag">Economics</li><li class="tag">Business administration</li>
          <li class="tag">The humanities</li>
        </ul>
      </div>
      <div class="split__media" data-reveal>{participants}
        <p class="figure-caption">Participants at a CSA Africa workshop</p>
      </div>
    </div>
  </div>
</section>

<section class="section band-dark">
  <div class="shell--wide">
    <div class="sec-head sec-head--split">
      <div data-reveal>
        <p class="num" style="color:var(--on-dark-2)">05 &#8212; After the workshop</p>
        <h2 class="h2" style="margin-top:1rem">Within 3&#8211;12 months, participants report&#8230;</h2>
      </div>
    </div>
    <ul class="checklist" data-reveal style="max-width:62ch">{after}</ul>
    <p class="lead" data-reveal style="margin-top:2.5rem;max-width:62ch">Many participants describe
      CSA Africa as a turning point in their technical skills, and in their belief that they belong in
      technology and can contribute meaningfully to its future.</p>
  </div>
</section>

<section class="section">
  <div class="shell--wide">
    <p class="eyebrow" data-reveal>What drives us</p>
    <div class="split" style="margin-top:2rem">
      <div data-reveal>
        <div class="split__media" style="margin-bottom:1.75rem">{vision}</div>
        <h3 class="h3">Our Vision</h3>
        <p class="lead" style="margin-top:.85rem">Our vision is a continent where every young African
          has the opportunity and capability to harness the power of computing.</p>
      </div>
      <div data-reveal>
        <div class="split__media" style="margin-bottom:1.75rem">{mission}</div>
        <h3 class="h3">Our Mission</h3>
        <p class="lead" style="margin-top:.85rem">To empower young Africans with transformative
          computing skills, providing them with the knowledge, resources, and mentorship needed to
          thrive in the information age.</p>
      </div>
    </div>
  </div>
</section>

{partners}
{cta}
""".format(
        hero=img("story/ibadan-2018", "The first CSA Africa workshop at the University of Ibadan, 2018", eager=True, sizes="100vw"),
        founder=img("story/founder-story", "Dr Sofiat Olaosebikan, founder of CSA Africa"),
        discovered=img("story/what-we-discovered", "Participants in a CSA Africa lecture hall"),
        participants=img("story/participants", "CSA Africa participants collaborating"),
        vision=img("story/vision", "Participants at a CSA Africa workshop"),
        mission=img("story/mission", "A CSA Africa workshop in progress"),
        after=after, partners=partner_wall(), cta=cta_band(),
    )
    return page("about.html", "About CSA Africa — three rejections and a decade in the dark",
                "How Computer Science Academy Africa started, what we discovered about the real "
                "barriers facing young Africans in tech, and the vision and mission that drive us.",
                body, "about", og_image="story/ibadan-2018")


# ------------------------------------------------------------------ team
def team():
    leads = "".join(
        '<article class="lead-card" data-reveal>'
        '<a href="{li}" target="_blank" rel="noopener" class="lead-card__img">{im}</a>'
        '<div><h3>{n}</h3><p class="role">{r}</p><span class="org">{o}</span>'
        '<a class="li-badge" href="{li}" target="_blank" rel="noopener">{ico} LinkedIn</a></div>'
        '</article>'.format(im=img(p, n), n=esc(n), r=esc(r), o=esc(o), li=li, ico=LI_ICON)
        for n, r, o, p, li in D.LEADERSHIP)

    vols = "".join(
        '<article class="person" data-reveal>'
        '<a class="person__img" href="{li}" target="_blank" rel="noopener" tabindex="-1" aria-hidden="true">{im}</a>'
        '<div><h3>{n}</h3><p>{r}</p>'
        '<a class="li-badge" href="{li}" target="_blank" rel="noopener">{ico} Profile</a></div>'
        '</article>'.format(im=img(p, n), n=esc(n), r=esc(r), li=li, ico=LI_ICON)
        for n, r, p, li in D.VOLUNTEERS)

    body = """
<section class="phero">
  <div class="phero__media">{hero}</div>
  <div class="phero__scrim"></div>
  <div class="shell--wide">
    <p class="eyebrow">Our team</p>
    <h1 class="h1">The people who make it happen</h1>
    <p class="phero__sub">Our success depends on these exceptional team of coordinators, instructors,
      tutors, and volunteers who give their time, and expertise to transform lives across the
      continent.</p>
  </div>
</section>

<section class="section" data-rail-wrap>
  <div class="shell--wide">
    <div class="sec-head sec-head--split">
      <div data-reveal>
        <p class="eyebrow">Leadership</p>
        <h2 class="h2">Our Leadership Team</h2>
      </div>
      <p class="lead" data-reveal>Meet the passionate minds behind CSA Africa.</p>
    </div>
    <div class="rail-head" data-reveal>
      <p class="num">{nleads} people<span class="rail-hint"> &#183; swipe or use the arrows</span></p>
      {lcontrols}
    </div>
    <div class="rail rail--leads" data-rail data-reveal-group tabindex="0" role="group"
         aria-label="Leadership team, scrollable">{leads}</div>
  </div>
</section>

<section class="section band-stone" data-rail-wrap>
  <div class="shell--wide">
    <div class="sec-head sec-head--split">
      <div data-reveal>
        <p class="eyebrow">Volunteers</p>
        <h2 class="h2">Our Past Workshop Volunteers</h2>
      </div>
      <p class="lead" data-reveal>Instructors, tutors and media volunteers from 2018 through 2025 &#8212;
        several of them CSA alumni who came back to teach.</p>
    </div>
    <div class="rail-head" data-reveal>
      <p class="num">{nvols} people<span class="rail-hint"> &#183; swipe or use the arrows</span></p>
      {vcontrols}
    </div>
    <div class="rail rail--people" data-rail data-reveal-group tabindex="0" role="group"
         aria-label="Past workshop volunteers, scrollable">{vols}</div>
  </div>
</section>

<section class="section--tight section">
  <div class="shell--wide">
    <div class="split" style="align-items:center">
      <div data-reveal>
        <p class="eyebrow">Join the team</p>
        <h2 class="h2">Teach a track. Tutor a cohort. Change a trajectory.</h2>
      </div>
      <div data-reveal>
        <p class="lead">Volunteers are the reason CSA Africa works. If you can teach, mentor,
          document or coordinate, we would like to hear from you.</p>
        <div class="btn-row" style="margin-top:1.75rem">
          <a class="btn" href="{volunteer}" target="_blank" rel="noopener">Apply as Volunteer {arw}</a>
          <a class="btn btn--ghost" href="contact.html">Contact the team {arw}</a>
        </div>
      </div>
    </div>
  </div>
</section>

{cta}
""".format(hero=img("story/team-hero", "The CSA Africa team and volunteers", eager=True, sizes="100vw"),
           leads=leads, vols=vols, nvols=len(D.VOLUNTEERS), nleads=len(D.LEADERSHIP),
           lcontrols=rail_controls("leadership team members"),
           vcontrols=rail_controls("volunteers"),
           volunteer=D.LINKS["volunteer"], arw=ARW, cta=cta_band())

    return page("team.html", "Team — CSA Africa",
                "The coordinators, instructors, tutors and volunteers behind Computer Science "
                "Academy Africa.", body, "team", og_image="story/team-hero")


# ------------------------------------------------------------------ news
def news():
    items = []
    for i, (title, im, excerpt, url, doc) in enumerate(D.NEWS):
        # Where we hold our own copy of the document, that is what the item
        # opens - it keeps working if the original host goes away. The source
        # URL stays available underneath, credited by name.
        href = ("assets/" + doc) if doc else url
        kind = "PDF" if doc else "Press"
        acts = ('<a class="tlink" href="{h}" target="_blank" rel="noopener">Read the article {arw}</a>'
                .format(h=href, arw=ARW))
        if doc:
            acts += ('<a class="tlink tlink--quiet" href="assets/{d}" download>Download PDF '
                     '<span class="mono">({sz})</span></a>'.format(d=doc, sz=filesize("assets/" + doc)))
            acts += ('<a class="tlink tlink--quiet" href="{u}" target="_blank" rel="noopener">'
                     'Original source {arw}</a>'.format(u=url, arw=ARW))
        items.append(
            '<article class="news-item{flip}" data-reveal>'
            '<div><span class="src">{n:02d} &#183; {k}</span></div>'
            '<div><h3>{t}</h3><p>{e}</p>'
            '<div class="news-item__acts">{acts}</div></div>'
            '<a class="news-item__img" href="{h}" target="_blank" rel="noopener" tabindex="-1" aria-hidden="true">{img}</a>'
            '</article>'.format(
                flip=" news-item--flip" if i % 2 else "", n=i + 1, t=esc(title), e=esc(excerpt),
                k=kind, h=href, acts=acts,
                img=img(im, title, sizes="(min-width: 820px) 360px, 100vw")))

    body = """
<section class="phero">
  <div class="phero__media">{hero}</div>
  <div class="phero__scrim"></div>
  <div class="shell--wide">
    <p class="eyebrow">News</p>
    <h1 class="h1">CSA Africa in the press</h1>
    <p class="phero__sub">Coverage of our workshops, our founder, and the participants building
      things after they leave the room.</p>
  </div>
</section>

<section class="section">
  <div class="shell--wide">
    <div class="news-list" data-reveal-group>{items}</div>
  </div>
</section>

<section class="section--tight section band-stone">
  <div class="shell--wide">
    <div class="split" style="align-items:center">
      <div data-reveal>
        <p class="eyebrow">Follow along</p>
        <h2 class="h2">Newer updates land on social first</h2>
      </div>
      <div data-reveal>
        <p class="lead">Workshop announcements, application calls and participant stories are posted
          across our channels.</p>
        <div class="socials" style="margin-top:1.5rem">{socials}</div>
      </div>
    </div>
  </div>
</section>

{cta}
""".format(hero=img("news/glasgow-news", "CSA Africa featured in the press", eager=True, sizes="100vw"),
           items="".join(items), socials=socials_html(), cta=cta_band())

    return page("news.html", "News — CSA Africa in the press",
                "Press coverage of Computer Science Academy Africa from the University of Glasgow, "
                "TechCabal, QS Top Universities, Metro, The Herald and more.",
                body, "news", og_image="news/glasgow-news")


# ------------------------------------------------------------------ inuka
def inuka_panels():
    """The documented panel sessions. The moderator's questions are distilled
    into themes in build_data - the run sheet itself is not public."""
    out = []
    for p in D.INUKA_PANELS:
        themes = "".join(
            '<div class="panel__voice"><h4>{n}</h4><p>{t}</p></div>'.format(n=esc(n), t=esc(t))
            for n, t in p["themes"])
        out.append(
            '<article class="panel" data-reveal>'
            '<div class="panel__head">'
            '<p class="panel__n">{day} &#183; {n}</p>'
            '<h3 class="panel__title">{title}</h3>'
            '<p class="panel__blurb">{blurb}</p>'
            '<p class="panel__meta"><span>{time}</span><span>Moderated by {mod}</span>'
            '<span class="panel__modrole">{modrole}</span></p>'
            '</div>'
            '<div class="panel__body">{themes}'
            '<p class="panel__closing"><span>Closing question</span>{closing}</p>'
            '</div></article>'.format(
                day=p["day"], n=p["n"], title=esc(p["title"]), blurb=esc(p["blurb"]),
                time=p["time"], mod=esc(p["moderator"][0]), modrole=esc(p["moderator"][1]),
                themes=themes, closing=p["closing"]))
    return "".join(out)


def inuka_people(sessions):
    """Full bio cards, for the organisers and the featured speaker."""
    return "".join(
        '<article class="speaker" data-reveal><div><h3 class="speaker__name">{n}</h3>'
        '<p class="speaker__role">{r}</p>{link}</div><div><p>{b}</p></div></article>'.format(
            n=esc(n), r=r, b=b,
            link=('<p style="margin-top:1rem"><a class="tlink" href="%s" target="_blank" '
                  'rel="noopener">Visit website %s</a></p>' % (u, ARW)) if u else "")
        for n, r, b, sess, u in D.INUKA_PEOPLE if sess in sessions)


def inuka_roster(sessions):
    """The long roster, compact.

    Eighteen full biographies is a wall of text on a page whose job is to say
    what happened. Name and role are always visible - that is what a visitor
    scanning the roster actually needs - and the biography opens on demand.
    Nothing is cut: choosing which half of someone's bio to show would mean
    editing their words, so the disclosure shows all of it or none."""
    return "".join(
        '<article class="person" data-reveal>'
        '<h3 class="person__name">{n}</h3><p class="person__role">{r}</p>{more}'
        '</article>'.format(
            n=esc(n), r=r,
            # Not everyone supplied a biography. They still led a session, so
            # they still get a card - it simply carries no disclosure.
            more=('<details class="person__more"><summary>Biography</summary>'
                  '<p>%s</p></details>' % b) if b else "")
        for n, r, b, sess, _u in D.INUKA_PEOPLE if sess in sessions)


def inuka():
    I = D.INUKA
    why = "".join('<p>%s</p>' % esc(p) for p in I["why"])
    beyond = "".join('<p>%s</p>' % esc(p) for p in I["beyond"])
    organisers = inuka_people(("organiser",))
    featured = inuka_people(("featured",))
    roster = inuka_roster(("mc", "panel-1", "panel-2", None))
    panels = inuka_panels()
    # Counted, not typed: these numbers described the roster wrongly the moment
    # the roster changed under them.
    n_people = len(D.INUKA_PEOPLE)
    roster_n = sum(1 for *_, sess, _u in D.INUKA_PEOPLE
                   if sess in ("mc", "panel-1", "panel-2", None))
    stat_rows = list(I["stats"])
    stat_rows.insert(1, (str(n_people), "Speakers, panellists and facilitators"))
    stats = "".join('<div class="stat" data-reveal><b>%s</b><span>%s</span></div>' % (v, esc(l))
                    for v, l in stat_rows)
    took = "".join('<li>%s</li>' % t for t in I["took_away"])
    facts = "".join('<li>%s</li>' % esc(t) for t in I["facts"])

    body = """
<section class="phero" style="min-height:clamp(460px,72vh,720px)">
  <div class="phero__media">{hero}</div>
  <div class="phero__scrim"></div>
  <div class="shell--wide">
    <p class="eyebrow"><span class="chip">{status}</span> {partners}</p>
    <h1 class="display" style="font-size:clamp(2.6rem,6.4vw,5.4rem)">INUKA Mombasa</h1>
    <p class="phero__sub serif-em" style="font-size:clamp(1.15rem,2vw,1.6rem);color:#fff">{tagline}</p>
    <div class="phero__meta">
      <span>{dates}</span><span>{venue}</span>
    </div>
  </div>
</section>

<section class="section--tight section">
  <div class="shell--wide">
    <p class="eyebrow" data-reveal>At a glance</p>
    <div class="stats-grid stats-grid--light" data-reveal-group style="margin-top:1.5rem">{stats}</div>
  </div>
</section>

<section class="section">
  <div class="shell--wide">
    <div class="split split--wide-text split--top">
      <div class="prose">
        <p class="eyebrow" data-reveal>Why it existed</p>
        <h2 class="h2" data-reveal style="max-width:18ch">Something no curriculum fixes</h2>
        <div data-reveal style="margin-top:1.75rem">{why}</div>
      </div>
      <div data-reveal>
        <div class="split__media"><div class="framed">{img1}</div></div>
      </div>
    </div>
  </div>
</section>

<section class="section band-dark">
  <div class="shell--narrow">
    <p class="eyebrow" data-reveal>Beyond the code</p>
    <div class="prose lead" data-reveal style="margin-top:1.25rem">{beyond}</div>
  </div>
</section>

<section class="section">
  <div class="shell--wide">
    <div class="sec-head sec-head--split">
      <div data-reveal>
        <p class="eyebrow">In the room</p>
        <h2 class="h2" style="max-width:16ch">Two panels, six voices</h2>
      </div>
      <p class="lead" data-reveal>Both panels were moderated by CSA Africa alumni from the
        2025 cohort &#8212; participants a year earlier, holding the microphone this time.</p>
    </div>
    <div class="panels" data-reveal-group>{panels}</div>
  </div>
</section>

<section class="section band-stone">
  <div class="shell--wide">
    <div class="sec-head sec-head--split">
      <div data-reveal>
        <p class="eyebrow">Whose idea this was</p>
        <h2 class="h2" style="max-width:18ch">The two behind INUKA</h2>
      </div>
      <p class="lead" data-reveal>One from each side of the partnership &#8212; CSA Africa and
        the NAA&#8217;M Initiative &#8212; and both of them proof of the thing the event
        set out to argue.</p>
    </div>
    {organisers}

    <div class="sec-head sec-head--split" style="margin-top:clamp(3.5rem,7vw,6rem)">
      <div data-reveal>
        <p class="eyebrow">Who they heard from</p>
        <h2 class="h2">People who have walked it</h2>
      </div>
    </div>
    {featured}
    <p class="lead" data-reveal style="margin-top:2.5rem;max-width:70ch">{also}</p>

    <div class="sec-head sec-head--split" style="margin-top:clamp(3.5rem,7vw,6rem)">
      <div data-reveal>
        <p class="eyebrow">The full roster</p>
        <h2 class="h2" style="max-width:20ch">Everyone who led a session</h2>
      </div>
      <p class="lead" data-reveal>{roster_n} more speakers, panellists and facilitators across
        the four days. Open any name to read their biography.</p>
    </div>
    <div class="people-grid" data-reveal-group>{roster}</div>
  </div>
</section>

<section class="section">
  <div class="shell--wide">
    <div class="split split--wide-text split--top">
      <div>
        <p class="eyebrow" data-reveal>What they took away</p>
        <h2 class="h2" data-reveal style="max-width:16ch">Four days, four things they keep</h2>
        <p class="lead" data-reveal style="margin-top:1.25rem">{note}</p>
        <ul class="checklist" data-reveal style="margin-top:2rem;max-width:64ch">{took}</ul>
      </div>
      <div data-reveal>
        <div class="split__media">{img2}</div>
        <ul class="facts" style="margin-top:1.5rem">{facts}</ul>
      </div>
    </div>
  </div>
</section>

{cta}
""".format(
        hero=img("story/inuka-hero", "INUKA Mombasa participants together", eager=True, sizes="100vw"),
        status=I["status"], partners=esc(I["partners"]), tagline=esc(I["tagline"]),
        dates=I["dates"], venue=esc(I["venue"]), stats=stats,
        why=why, beyond=beyond, took=took, facts=facts, note=esc(I["took_away_note"]),
        organisers=organisers, featured=featured, roster=roster, roster_n=roster_n,
        panels=panels, also=esc(I["also"]),
        img1=img("story/peer-learning", "INUKA Mombasa participants working side by side"),
        img2=img("story/cohort", "Participants together at the close of INUKA Mombasa"),
        cta=cta_band())

    return page("inuka-mombasa.html", "INUKA Mombasa 2026 — Believe. See. Build. Rise.",
                "CSA Africa's first mindset transformation event, in partnership with NAA'M "
                "Initiative and Swahilipot Hub Foundation. 10-13 September, Mombasa, Kenya. Free to "
                "attend, no coding required.", body, "inuka", og_image="story/inuka-hero")


# ------------------------------------------------------------------ workshops
def workshops():
    tracks = "".join('<li><div class="row"><span class="n">%02d</span><h3>%s</h3></div></li>'
                     % (i, esc(t)) for i, t in enumerate(D.TRACKS, 1))
    timeline = "".join('<li data-reveal><span class="n">Step %02d</span><h3>%s</h3><p>%s</p></li>'
                       % (i, esc(w), esc(d)) for i, (w, d) in enumerate(D.TIMELINE, 1))
    support = "".join('<div class="feat" data-reveal><span class="n">%02d</span><h3>%s</h3><p>%s</p></div>'
                      % (i, esc(t), esc(b)) for i, (t, b) in enumerate(D.SUPPORT, 1))
    gains = "".join('<div class="feat" data-reveal><span class="n">%02d</span><h3>%s</h3><p>%s</p></div>'
                    % (i, esc(t), esc(b)) for i, (t, b) in enumerate(D.GAINS, 1))
    after = "".join('<li>%s</li>' % esc(t) for t in D.AFTER_WORKSHOP)

    editions = []
    for e in D.EDITIONS:
        if not e["slug"]:
            editions.append(
                '<article class="edition edition--soon" data-reveal>'
                '<span class="edition__tag" style="background:var(--navy);color:#fff">%s</span>'
                '<div class="edition__year">%s</div><p class="edition__place">%s</p>'
                '<span class="edition__more">Applications open Jan / Feb</span></article>'
                % (e["tag"], e["year"], e["place"]))
        else:
            editions.append(
                '<a class="edition" href="{s}.html" data-reveal><span class="edition__img">{im}</span>'
                '<div class="edition__year">{y}</div><p class="edition__place">{p}<br>{d}</p>'
                '<span class="edition__more">View the edition {arw}</span></a>'.format(
                    s=e["slug"], y=e["year"], p=esc(e["place"]), d=esc(e["dates"]),
                    im=img(e["img"], "CSA Africa %s" % e["year"]), arw=ARW))

    body = """
<section class="phero">
  <div class="phero__media">{hero}</div>
  <div class="phero__scrim"></div>
  <div class="shell--wide">
    <p class="eyebrow">Python workshops</p>
    <h1 class="h1">Three weeks. Five tracks. One continent.</h1>
    <p class="phero__sub">CSA Africa runs annual three-week Python programming workshops in
      collaboration with host universities across Africa.</p>
  </div>
</section>

<section class="section">
  <div class="shell--wide">
    <div class="split split--wide-text split--top">
      <div class="prose">
        <p class="eyebrow" data-reveal>How we work</p>
        <h2 class="h2" data-reveal style="max-width:16ch">Hosted by universities, built for
          beginners and beyond</h2>
        <p class="lead" data-reveal style="margin-top:1.5rem">We&#8217;ve partnered with institutions
          in Nigeria, Rwanda, and Kenya, with plans to expand further across the continent.</p>
        <p data-reveal style="margin-top:1.25rem;color:var(--ink-2)">Our three-week workshops are
          intensive and hands-on with multiple tracks catering to different experience levels:</p>
        <ul class="tracks" data-reveal style="margin-top:1.25rem">{tracks}</ul>
      </div>
      <div class="split__media" data-reveal><div class="framed">{img1}</div>
        <p class="figure-caption">Hands-on coding &#183; CSA Africa</p>
      </div>
    </div>
  </div>
</section>

<section class="section band-dark">
  <div class="shell--wide">
    <div class="sec-head sec-head--split">
      <div data-reveal>
        <p class="eyebrow">Our workshop model</p>
        <h2 class="h2">Two weeks of learning. One week of building.</h2>
      </div>
    </div>
    <div class="split" data-reveal-group>
      <div data-reveal>
        <p class="num" style="color:var(--amber)">WEEK 1&#8211;2</p>
        <h3 class="h3" style="margin-top:.9rem;color:#fff">Learning &amp; doing</h3>
        <p class="lead" style="margin-top:1rem">Each track combines live instruction with extensive
          hands-on coding sessions. International instructors from the University of Glasgow and
          other UK institutions work alongside in-country tutors who provide personalised support.</p>
      </div>
      <div data-reveal>
        <p class="num" style="color:var(--amber)">WEEK 3</p>
        <h3 class="h3" style="margin-top:.9rem;color:#fff">Building &amp; presenting</h3>
        <p class="lead" style="margin-top:1rem">Participants form diverse teams and spend the final
          week developing projects that address real challenges in their communities. On the final
          day, teams present their work by showing their code, defending their design decisions,
          explaining their problem-solving process, and demonstrating impact potential.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell--wide">
    <p class="eyebrow" data-reveal>Application timeline</p>
    <ul class="timeline" data-reveal-group style="margin-top:1.5rem">{timeline}</ul>

    <div class="sec-head sec-head--split" style="margin-top:clamp(3.5rem,7vw,6rem)">
      <div data-reveal>
        <p class="eyebrow">Comprehensive support</p>
        <h2 class="h2">Nobody should miss out on logistics</h2>
      </div>
      <p class="lead" data-reveal>The workshop is free at the point of need. What usually stops
        people from attending, we cover.</p>
    </div>
    <div class="feat-grid feat-grid--4" data-reveal-group>{support}</div>
  </div>
</section>

<section class="section band-stone">
  <div class="shell--wide">
    <div class="split split--flip split--top">
      <div class="prose">
        <p class="eyebrow" data-reveal>Our participants</p>
        <h2 class="h2" data-reveal>Who the workshops are for</h2>
        <div data-reveal style="margin-top:1.5rem">
          <p>CSA Africa workshops are designed for university students, early-career researchers, and
            professionals who are eager to build their programming confidence and apply computing
            skills to their studies, research, or work.</p>
          <p>Our participants come from diverse academic backgrounds: mathematics, engineering,
            medicine, pharmacy, nursing, law, economics, business administration, and the humanities.</p>
        </div>
      </div>
      <div class="split__media" data-reveal>{img2}</div>
    </div>

    <div style="margin-top:clamp(3rem,6vw,5rem)">
      <p class="eyebrow" data-reveal>What participants gain</p>
      <div class="feat-grid feat-grid--4" data-reveal-group style="margin-top:1.5rem">{gains}</div>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell--wide">
    <div class="split split--top">
      <div>
        <p class="eyebrow" data-reveal>After the workshop</p>
        <h2 class="h2" data-reveal style="max-width:18ch">Within 3&#8211;12 months, participants
          report&#8230;</h2>
      </div>
      <div data-reveal>
        <ul class="checklist">{after}</ul>
        <p class="lead" style="margin-top:2rem">Many participants describe CSA Africa as a turning
          point in their technical skills, and in their belief that they belong in technology and can
          contribute meaningfully to its future.</p>
      </div>
    </div>
  </div>
</section>

<section class="section band-stone">
  <div class="shell--wide">
    <div class="sec-head sec-head--split">
      <div data-reveal>
        <p class="eyebrow">Every edition</p>
        <h2 class="h2">Past and future workshops</h2>
      </div>
    </div>
    <div class="card-grid card-grid--editions" data-reveal-group>{editions}</div>
  </div>
</section>

<section class="section--tight section band-dark">
  <div class="shell--wide">
    <div class="split" style="align-items:center">
      <div data-reveal>
        <p class="eyebrow">Join our waitlist</p>
        <h2 class="h2">Be the first to know when applications open</h2>
      </div>
      <div data-reveal>
        <form class="inline-form" data-mailto="{email}" data-subject="Waitlist: CSA Africa Python Workshop">
          <div class="field" style="flex:1 1 240px">
            <label for="wl-email">Email</label>
            <input id="wl-email" name="email" data-label="Email" type="email" required
                   placeholder="you@example.com" autocomplete="email">
          </div>
          <button class="btn btn--amber" type="submit" style="align-self:end">Join waitlist {arw}</button>
          <p class="form__note" data-form-status style="flex:1 1 100%;color:var(--on-dark-2)">
            We will notify you when the next call for applications opens.</p>
        </form>
      </div>
    </div>
  </div>
</section>

{cta}
""".format(hero=img("story/workshops-hero", "A CSA Africa Python workshop in session", eager=True, sizes="100vw"),
           tracks=tracks, timeline=timeline, support=support, gains=gains, after=after,
           editions="".join(editions), email=D.EMAIL, arw=ARW,
           img1=img("story/classroom", "Participants coding during a CSA Africa workshop"),
           img2=img("story/participants", "CSA Africa participants working together"),
           cta=cta_band())

    return page("workshops.html", "Python Workshops — CSA Africa",
                "Annual three-week Python programming workshops hosted with universities across "
                "Africa: five tracks, full accommodation, childcare and travel support.",
                body, "workshops", og_image="story/workshops-hero")


# ------------------------------------------------------------------ editions
def edition(year):
    e = D.EDITION_PAGES[year]
    stats = "".join('<div class="stat" data-reveal><b>%s</b><span>%s</span></div>' % (v, esc(l))
                    for v, l in e["stats"])
    highlights = ""
    if e["highlights"]:
        highlights = """
<section class="section">
  <div class="shell--wide">
    <div class="split split--top">
      <div data-reveal>
        <p class="eyebrow">Highlights</p>
        <h2 class="h2" style="max-width:14ch">What happened in the room</h2>
      </div>
      <ul class="hl-list" data-reveal>{items}</ul>
    </div>
  </div>
</section>""".format(items="".join('<li>%s</li>' % esc(t) for t in e["highlights"]))

    video = ""
    if e["video"]:
        vid, poster, label = e["video"]
        video = """
<section class="section--tight section band-dark">
  <div class="shell--wide">
    <div class="sec-head sec-head--split">
      <div data-reveal><p class="eyebrow">Film</p><h2 class="h2">{label}</h2></div>
    </div>
    <div style="max-width:960px" data-reveal>{facade}</div>
  </div>
</section>""".format(label=esc(label), facade=video_facade(
            vid, poster, label,
            alt="The full CSA Africa 2025 cohort together at the University of Nairobi",
            sizes="(min-width: 1040px) 960px, 100vw",
            # the <h2> directly above already names the film; repeating it over
            # the photograph only veils the people in it
            show_label=False))

    others = "".join(
        '<a class="edition" href="{s}.html" data-reveal><span class="edition__img">{im}</span>'
        '<div class="edition__year">{y}</div><p class="edition__place">{p}</p>'
        '<span class="edition__more">View the edition {arw}</span></a>'.format(
            s=o["slug"], y=o["year"], p=esc(o["place"]),
            im=img(o["img"], "CSA Africa %s" % o["year"]), arw=ARW)
        for o in D.EDITIONS if o["slug"] and o["year"] != year)

    body = """
<section class="phero">
  <div class="phero__media">{hero}</div>
  <div class="phero__scrim"></div>
  <div class="shell--wide">
    <p class="eyebrow"><a href="workshops.html" style="color:inherit">Python Workshops</a></p>
    <h1 class="display" style="font-size:clamp(2.6rem,6.6vw,5.6rem)">{title}</h1>
    <div class="phero__meta"><span>{place}</span><span>{dates}</span></div>
  </div>
</section>

<section class="section--tight section">
  <div class="shell--wide">
    <p class="eyebrow" data-reveal>At a glance</p>
    <div class="stats-grid stats-grid--light" data-reveal-group style="margin-top:1.5rem">{stats}</div>
  </div>
</section>

{highlights}
{video}

<section class="section band-stone">
  <div class="shell--wide">
    <div class="sec-head sec-head--split">
      <div data-reveal><p class="eyebrow">Photo gallery</p>
        <h2 class="h2">{year} in photographs</h2></div>
      <p class="lead" data-reveal>Select any photograph to view it full size.</p>
    </div>
    <div data-reveal>{gallery}</div>
  </div>
</section>

<section class="section">
  <div class="shell--wide">
    <div class="sec-head sec-head--split">
      <div data-reveal><p class="eyebrow">Other editions</p>
        <h2 class="h2">Explore the rest</h2></div>
    </div>
    <div class="card-grid card-grid--editions" data-reveal-group>{others}</div>
  </div>
</section>

<section class="section--tight section band-dark">
  <div class="shell--wide">
    <div class="split" style="align-items:center">
      <div data-reveal>
        <p class="eyebrow">Join our waitlist</p>
        <h2 class="h2">Be the first to know when applications open</h2>
      </div>
      <div data-reveal>
        <form class="inline-form" data-mailto="{email}" data-subject="Waitlist: CSA Africa Python Workshop">
          <div class="field" style="flex:1 1 240px">
            <label for="wl-email">Email</label>
            <input id="wl-email" name="email" data-label="Email" type="email" required
                   placeholder="you@example.com" autocomplete="email">
          </div>
          <button class="btn btn--amber" type="submit" style="align-self:end">Join waitlist {arw}</button>
          <p class="form__note" data-form-status style="flex:1 1 100%;color:var(--on-dark-2)">
            We will notify you when the next call for applications opens.</p>
        </form>
      </div>
    </div>
  </div>
</section>

{cta}
""".format(hero=img(e["hero"], "%s, %s" % (e["title"], e["place"]), eager=True, sizes="100vw"),
           title=esc(e["title"]), place=esc(e["place"]), dates=e["dates"],
           stats=stats, highlights=highlights, video=video, year=year,
           gallery=gallery_block(year, e["count"], e["title"]),
           others=others, email=D.EMAIL, arw=ARW, cta=cta_band())

    return page("csa-%s.html" % year, "%s — %s" % (e["title"], e["place"]),
                "%s took place at %s, %s. Participants, tracks, highlights and the full photo "
                "gallery." % (e["title"], e["place"], e["dates"]),
                body, "csa-%s" % year, og_image=e["hero"])


# ------------------------------------------------------------------ contact
def contact():
    body = """
<section class="section" style="padding-top:clamp(3rem,7vw,6rem)">
  <div class="shell--wide">
    <div class="split split--wide-text split--top">
      <div>
        <p class="eyebrow" data-reveal>Contact us</p>
        <h1 class="h1" data-reveal style="max-width:14ch">Let&#8217;s build the next cohort together</h1>
        <p class="lead" data-reveal style="margin-top:1.5rem;max-width:46ch">Kindly fill the form
          below to reach out to us or send us an email.</p>
        <a class="footer-mail" href="mailto:{email}" data-reveal style="font-size:1.15rem">{email}</a>

        <div data-reveal style="margin-top:2.75rem">
          <h2 class="h3">Where we are</h2>
          <p style="margin-top:.75rem;color:var(--ink-2);max-width:40ch">{about}</p>
        </div>

        <div data-reveal style="margin-top:2.25rem">
          <h2 class="h3">Follow CSA Africa</h2>
          <div class="socials" style="margin-top:1rem">{socials}</div>
        </div>
      </div>

      <div data-reveal>
        <form class="form form--2" data-mailto="{email}" data-subject="Website enquiry — CSA Africa"
              style="background:var(--white);border:1px solid var(--line-soft);border-radius:5px;padding:clamp(1.5rem,3vw,2.25rem)">
          <div class="field">
            <label for="fn">First name *</label>
            <input id="fn" name="first_name" data-label="First name" type="text" required autocomplete="given-name">
          </div>
          <div class="field">
            <label for="ln">Last name *</label>
            <input id="ln" name="last_name" data-label="Last name" type="text" required autocomplete="family-name">
          </div>
          <div class="field full">
            <label for="em">Email *</label>
            <input id="em" name="email" data-label="Email" type="email" required autocomplete="email">
          </div>
          <div class="field full">
            <label for="msg">Message *</label>
            <textarea id="msg" name="message" data-label="Message" required></textarea>
          </div>
          <div class="full">
            <button class="btn btn--amber" type="submit">Send message {arw}</button>
            <p class="form__note" data-form-status style="margin-top:.9rem">This opens your email app
              with the message ready to send.</p>
          </div>
        </form>
      </div>
    </div>
  </div>
</section>

<section class="section--tight section band-stone">
  <div class="shell--wide">
    <div class="sec-head sec-head--split">
      <div data-reveal><p class="eyebrow">Three ways in</p>
        <h2 class="h2">Work with us</h2></div>
    </div>
    <div class="feat-grid" data-reveal-group>
      <div class="feat" style="background:var(--paper-2)">
        <span class="n">01</span><h3>Volunteer</h3>
        <p>Teach a track, tutor a cohort, or help us document the work.</p>
        <p style="margin-top:1rem"><a class="tlink" href="{volunteer}" target="_blank" rel="noopener">Apply as Volunteer {arw}</a></p>
      </div>
      <div class="feat" style="background:var(--paper-2)">
        <span class="n">02</span><h3>Partner</h3>
        <p>Host a workshop, fund a cohort, or open doors for our alumni.</p>
        <p style="margin-top:1rem"><a class="tlink" href="mailto:{email}">Email the team {arw}</a></p>
      </div>
      <div class="feat" style="background:var(--paper-2)">
        <span class="n">03</span><h3>Donate</h3>
        <p>Cover a seat, a bed, a bus fare, or childcare for a participant.</p>
        <p style="margin-top:1rem"><a class="tlink" href="{donate}" target="_blank" rel="noopener">Make a Donation {arw}</a></p>
      </div>
    </div>
  </div>
</section>
""".format(email=D.EMAIL, about=esc(D.FOOTER_ABOUT), socials=socials_html(),
           volunteer=D.LINKS["volunteer"], donate=D.LINKS["donate"], arw=ARW)

    return page("contact.html", "Contact — CSA Africa",
                "Get in touch with Computer Science Academy Africa: partner with us, volunteer, or "
                "support the work. Email csacademyafrica@gmail.com.", body, "contact")


# ------------------------------------------------------------------ 404
def notfound():
    body = """
<section class="section" style="padding-block:clamp(5rem,14vw,10rem)">
  <div class="shell--narrow" style="text-align:center">
    <p class="eyebrow eyebrow--plain" style="justify-content:center">Error 404</p>
    <h1 class="display" style="font-size:clamp(3rem,10vw,7rem)">01 00</h1>
    <p class="lead" style="margin-top:1.5rem">That page isn&#8217;t here. It may have moved, or the
      link may be out of date.</p>
    <div class="btn-row" style="margin-top:2rem;justify-content:center">
      <a class="btn" href="index.html">Back to home {arw}</a>
      <a class="btn btn--ghost" href="workshops.html">Browse the workshops {arw}</a>
    </div>
  </div>
</section>""".format(arw=ARW)
    return page("404.html", "Page not found — CSA Africa",
                "The page you were looking for could not be found.", body, "none")


# ------------------------------------------------------------------ run
def main():
    pages = [home(), about(), team(), news(), inuka(), workshops(), contact(), notfound()]
    for y in ["2025", "2022", "2021", "2019", "2018"]:
        pages.append(edition(y))

    urls = "".join(
        "  <url><loc>%s/%s</loc><changefreq>monthly</changefreq></url>\n" % (SITE, p)
        for p in pages if p != "404.html")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls)

    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE)

    print("built %d pages:" % len(pages))
    for p in sorted(pages):
        print("  ", p)


if __name__ == "__main__":
    main()
