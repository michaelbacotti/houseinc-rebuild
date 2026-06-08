# HOUSE, Inc. — Site Memory

> Local notes for the rebuild. Not deployed.

## Source of Truth

- **Authoritative folder:** `entities/house/website/`
- **GitHub repo:** `michaelbacotti/houseinc-rebuild`
- **CF Pages project:** `houseinc-rebuild`
- **Primary domain:** `houseinc501c3.com` (CF Pages custom domain, SSL active)
- **Secondary domain:** `houseinc501c3.org` (CF Pages custom domain, SSL active — currently serves same site, canonical tags point to .com)
- **Initial deploy URL:** `https://houseinc-rebuild.pages.dev/`
- **DNS:** Both domains moved from Squarespace to Cloudflare nameservers (paul.ns.cloudflare.com, autumn.ns.cloudflare.com)
- **SSL:** Auto-issued by Google CA via CF Pages

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
2. **Verified email addresses (current state, 2026-06-08):**
   - `donations@houseinc501c3.com` — confirmed in Master File, set up in iCloud
   - `info@houseinc501c3.com` — set up in iCloud
   - `help@houseinc501c3.com` and `board@houseinc501c3.com` — **collapsed to `info@`** in the site. Apply page and Board page now both use `info@` with prefilled subject lines (`Rental Assistance Request`, `Board Governance`). Mike can add `help@` as a friendlier alias later (~2 min in iCloud Settings → Custom Email Domain) if he wants — it would not require any code change, just adding the alias in iCloud and optionally re-pointing the mailto. **See Workboard card "HOUSE Email" for the full decision context.**
   - **Architecture decision:** For a small 501(c)(3), use one iCloud inbox with multiple role-based aliases. iCloud+ Custom Email Domain routes all aliases to the same inbox. Mailto links with prefilled `?subject=` carry the subcategory (Rental Assistance, Board Governance, etc.) — same UX as separate mailboxes, but no forwarding plumbing required.
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

## Domain Architecture (current state, 2026-06-08)

Both `houseinc501c3.com` and `houseinc501c3.org` are attached as custom domains to the `houseinc-rebuild` CF Pages project. Both serve the **same site** (single source of truth). Every page has `<link rel="canonical" href="https://houseinc501c3.com/...">` so Google consolidates all search equity to .com.

**Why both, with .com as primary:**
- `.com` has accumulated brand recognition and donor mindshare from the Squarespace era
- `.org` exists for board members / donors / IRS records that may reference it
- Both serve → no donor is ever "404 not found" regardless of which they type
- Canonical tag prevents duplicate-content SEO penalty
- Single deploy pipeline serves both (one repo, one project, one `git push`)

**Decision recorded:** Mike originally asked about making .org primary. Recommendation was to keep .com primary and park .org as a secondary serving the same site. This is what shipped.

## Domain Migration Steps (executed 2026-06-08)

1. ✅ Mike reviewed site at `https://houseinc-rebuild.pages.dev/`
2. ✅ Mike confirmed content (donate page, contact, transparency, etc. all approved)
3. ✅ Mike moved `houseinc501c3.com` DNS to Cloudflare (changed nameservers at Squarespace registrar to Cloudflare NS)
4. ✅ Mike moved `houseinc501c3.org` DNS to Cloudflare (same procedure)
5. ✅ Mike added both custom domains in CF Pages project settings
6. ✅ SSL certificates auto-issued (Google CA, ~5 min)
7. ✅ Both `https://houseinc501c3.com/` and `https://houseinc501c3.org/` resolve to the new site
8. ⏳ **TODO: Cancel Squarespace subscription** (recommend waiting 30 days to confirm no broken-link reports)

## Squarespace Cutover Checklist

- [x] DNS moved to Cloudflare (both domains)
- [x] New site live on both domains
- [ ] Export Squarespace content (built-in export, save backup)
- [ ] Screenshot the Squarespace site for archival
- [ ] Wait 30 days for any broken-link reports
- [ ] Cancel Squarespace subscription
- [ ] Confirm Squarespace DNS removal doesn't affect us (we own DNS now)

---
_Last updated: 2026-06-08 (post domain migration)
