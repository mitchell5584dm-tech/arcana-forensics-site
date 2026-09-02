# Arcana Forensics

Offline-first digital forensics, incident-response, and security-awareness tools for individuals, small businesses, labs, and investigators.

- Website: https://arcana-forensics.com/
- GitHub organization/profile: https://github.com/mitchell5584dm-tech
- Product source and releases: https://github.com/mitchell5584dm-tech/Security-Operations-Forensics-Toolkit
- Security reports: see [SECURITY.md](SECURITY.md)
- Verified links: see [LINKS.md](LINKS.md)

## Products currently linked

| Product | Price | Checkout |
|---|---:|---|
| CredentialAuditor Pro | 14 days free, then $99/year | Verified Stripe Payment Link |
| PASTE TRAP Standard / SMB Kit | $499 one time | Verified Stripe Payment Link |
| PASTE TRAP Pro / Enterprise Kit | $999 one time | Verified Stripe Payment Link |

The site must not send a visitor to a checkout whose Stripe product or price differs from the label on the button.

## Repository structure

- `index.html`: main public landing page
- `store.html`: verified product catalog
- `pastetrap/`: PASTE TRAP landing page and media
- `privacy.html`, `terms.html`, `refunds.html`: customer policies
- `sitemap.xml`, `image-sitemap.xml`, `robots.txt`: search discovery
- `webapp/`: legacy/prototype application files; not the canonical public landing page

## Local review

Serve the repository with any static server, then check every internal link, page title, canonical URL, checkout label, and release download. Do not place secrets, customer data, Stripe secret keys, or internal Git metadata in this repository.

## Release checklist

1. Confirm all Payment Links in Stripe and record the product, billing interval, amount, currency, and post-payment redirect in `LINKS.md`.
2. Run link and HTML validation.
3. Review security, privacy, terms, and refund language.
4. Update `sitemap.xml` dates only for pages materially changed.
5. Merge through a reviewed pull request.
