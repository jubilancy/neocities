# basedgirl.neocities.org

Jekyll site, forked from [tomcritchlow/tomcritchlow.github.io](https://github.com/tomcritchlow/tomcritchlow.github.io)
and reorganised so the repo root is four files instead of eighty. Built by GitHub
Actions, deployed to [Neocities](https://neocities.org).

---

## Layout

```
.
├── _config.yml          # the only config
├── Gemfile
├── README.md
├── .github/workflows/
│   └── deploy.yml       # build -> deploy to Neocities on push to main
├── _data/
│   ├── nav.yml          # the left-hand nav
│   └── graphics.yml     # OPTIONAL gallery display names
├── _includes/           # head, nav, footer, wiki + writing chrome
├── _layouts/            # blog, wiki, library, links, projects, gallery, tufte
├── _pages/              # every standalone page (see note below)
├── _plugins/
│   └── graphics_gallery.rb   # auto-generates the gallery pages
├── _posts/              # blog: YYYY-MM-DD-slug.md
├── _wiki/<folder>/      # digital garden, grouped by folder
├── _library/            # saved things, fuzzy-searchable
├── _links/              # link + quote stream
├── _blogchains/         # linked post series
├── _projects/
├── assets/
│   ├── css/  js/  fonts/  img/
├── graphics/            # the gallery source images
│   ├── blinkies/  stickers/  pixels/  88x31/
│   └── banners/  dividers/  stamps/  cursors/
└── scripts/
    └── fetch_feeds.py   # builds the data behind /feeds
```

**One rule about `_pages/`:** underscore folders are invisible to Jekyll unless
listed under `include:` in `_config.yml`, and pages inside them do not get a
sensible URL for free. So **every file in `_pages/` must declare its own
`permalink:`** in front matter. Add a page, add a permalink. That's the whole
tax for a clean root.

---

## The graphics gallery

Make a folder under `graphics/`. Drop images in. Push. Done.

`_plugins/graphics_gallery.rb` scans `graphics/*` at build time and generates a
page at `/graphics/<folder>/` for every folder holding at least one image
(`.gif .png .jpg .jpeg .webp .avif .svg .apng`). `/graphics/` lists them all.
An empty folder is simply not published, so the eight starter folders stay
invisible until you fill them.

There is **no index to maintain and no config to edit** to add a category.
`_data/graphics.yml` is optional and only overrides the display name or adds a
blurb — an unlisted folder still appears, named after itself.

Clicking any image copies its full URL, which is the useful thing for buttons
and blinkies.

> Local plugins run here because GitHub Actions runs `jekyll build` itself. This
> would **not** work on GitHub Pages, which only permits whitelisted plugins.

---

## Deploying

1. Neocities → Settings → API → generate your key.
2. GitHub repo → Settings → Secrets and variables → Actions → New repository
   secret, named **`NEOCITIES_API_KEY`**.
3. Push to `main`.

`deploy.yml` uses [`bcomnes/deploy-to-neocities@v3`](https://github.com/bcomnes/deploy-to-neocities)
with `cleanup: true`, so anything deleted here is deleted from the live site.
It also runs daily on a cron to refresh `/feeds`.

## Running it locally

```bash
bundle install
bundle exec jekyll serve      # http://localhost:4000

# optional, populates /feeds
pip install feedparser && python scripts/fetch_feeds.py
```

---

## Neocities constraints worth knowing

- **Free accounts only accept whitelisted file extensions**
  ([list](https://neocities.org/site_files/allowed_types)). `.xsl`, `.mp3`,
  `.mp4`, `.cur` and `.ani` are all out — which is why the original repo's
  `feed.xsl` didn't survive the fork. The deploy action filters unsupported
  files rather than failing, so a stray file goes quietly missing.
- **`connect-src 'self'`.** Free sites get a CSP that blocks `fetch()`/XHR to
  any other domain, and `form-action 'self'` blocks posting forms off-site.
  External `<script src>`, stylesheets, fonts and images are all still fine
  (`script-src *`), and iframes work. This is why `/feeds` is rendered at build
  time from `_data/feeds.json` instead of fetching in the browser.
- **1GB storage, 200GB bandwidth**, custom domains are supporters-only.

## What was cut from the fork

Six abandoned homepage drafts, two 760KB `index-2023` files, `.DS_Store`,
`.obsidian/`, `.vscode/`, `Untitled.md`, the consulting/advisor/workshops
business pages, the AMP stories collection (AMP is dead), `feed.xsl`, Tom's
Google Analytics/Plausible, his Commento and Hypothesis embeds, his Buttondown
signup forms, and 179MB of images that no surviving page referenced. Two or
three items of each content type were kept as format examples — they are Tom's
words, so replace them when convenient.
