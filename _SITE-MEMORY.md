# HOUSE, Inc. — Site Memory

> Local notes for the rebuild. Not deployed.

## Source of Truth

- **Authoritative folder:** `entities/house/website/`
- **GitHub repo:** `michaelbacotti/houseinc-rebuild`
- **CF Pages project:** `houseinc-rebuild`
- **Domain:** `houseinc501c3.com` (current Squarespace → migrate to CF Pages)
- **Initial deploy URL:** `https://houseinc-rebuild.pages.dev/`

## Build Pattern

Static HTML, no build.py (Pattern C per `memory/website-standards-doctrine.md`).

Pages are hand-edited. The only generated artifact is `sitemap.xml` (run `python3 generate_sitemap.py` after adding/removing pages).

## Pages (9)

| Path | File | Purpose |
|---|---|---|
| `/` | `index.html` | Homepage — mission, stats, how-to-help, apply CTA |
| `/mission/` | `mission/index.html` | Mission, beliefs, who we help |
| `/programs/` | `programs/index.html` | ERAP, zero-interest forgivable loans, case coordination |
| `/apply/` | `apply/index.html` | How to apply, eligibility, what we need |
| `/donate/` | `donate/index.html` | Donation methods, tax info, fraud warning |
| `/stories/` | `stories/index.html` | Aggregate impact — no individual names without consent |
| `/transparency/` | `transparency/index.html` | EIN, governance, 990, banking, donor privacy |
| `/board/` | `board/index.html` | Board & governance — no public roster by default |
| `/contact/` | `contact/index.html` | Email, phone, mail, social, crisis resources |

## Content Discipline

- No individual applicant names on the public site
- No individual case details unless explicit, documented consent
- No AdSense (501(c)(3) — mission-first, no ads)
- No GA4 (privacy-respecting for now — can be added later)
- Aggregate stats only: 9 families, ~22 individuals, $22,400+ disbursed

## Open Items (must be resolved by Mike)

1. **Current board roster** — Master Organizer lists 5 active, but Inge Thomas resigned April 6, 2026 per `entities/house/references/house-inc.md`. The Board page intentionally does NOT publish a roster — it directs people to email for the current list. Mike should confirm whether to publish a public roster on the site or keep the current "request by email" approach.
2. **Verified email addresses:**
   - `donations@houseinc501c3.com` — confirmed in Master File
   - `help@houseinc501c3.com` — created for the apply page, **needs Mike to set up**
   - `info@houseinc501c3.com` — created for the contact page, **needs Mike to set up**
   - `board@houseinc501c3.com` — created for the board page, **needs Mike to set up**
3. **990-N filing status** — entity reference flags 2023 filing as unconfirmed. Transparency page mentions filings honestly but does not invent dates. Mike should verify with Anderson Advisors before publishing any specific year.
4. **Founding date** — Squarespace said "July 2021"; canonical entity reference says "~2022". I have used neither specific date on the public site (mission page just says "founded"). Mike should confirm.
5. **"HOUSE" New Hampshire trade name** — registered. Renewal $50 due Sep 29, 2026 (per `entities/house/references/house-inc.md`).
6. **Ali Cali** — candidate for the open board seat (per entity reference). Not mentioned on the public site.

## Deploy Workflow

```bash
cd /Users/mike/.openclaw/workspace-bacottibot/entities/house/website

# 1. Edit files
# 2. (if you add/remove pages) regenerate sitemap:
python3 generate_sitemap.py

# 3. Commit and push
git add -A
git commit -m "Describe your change"
git push

# 4. CF Pages auto-deploys in ~2 minutes
# 5. Verify: https://houseinc-rebuild.pages.dev/
```

## Standards Compliance

Per `memory/website-standards-doctrine.md`:
- ✅ `index.html`, `style.css`, `nav.js`, `footer.js`
- ✅ `sitemap.xml` (all URLs end with `/`)
- ✅ `robots.txt` (CF Pages standard)
- ✅ `_redirects` (`*.html` → `*/`)
- ✅ `og-image.jpg` (1200x630)
- ✅ No AdSense (501(c)(3) exception — like bacotti.com)
- ✅ No GA4 (privacy choice for now)
- ✅ Mobile-responsive (mobile < 768, tablet 768-1024, desktop > 1024)
- ✅ Single CSS file, no inline styles
- ✅ Canonical URL on every page (absolute, trailing slash)
- ✅ Meta description + og:title + og:description + og:url on every page

## Domain Migration Steps (post-Mike-approval)

1. Mike reviews site at `https://houseinc-rebuild.pages.dev/`
2. Mike confirms any content gaps filled
3. Mike moves `houseinc501c3.com` DNS to Cloudflare (if not already there)
4. Mike adds custom domain in CF Pages project settings
5. Wait for SSL provisioning (~5 min)
6. Verify https://houseinc501c3.com/ resolves
7. Cancel Squarespace subscription

---
_Last updated: 2026-06-08_
