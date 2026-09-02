# Verified link registry

Last audited: 2026-09-01

## Canonical destinations

- Production site: https://arcana-forensics.com/
- Repository: https://github.com/mitchell5584dm-tech/arcana-forensics-site
- Product source/releases: https://github.com/mitchell5584dm-tech/Security-Operations-Forensics-Toolkit

## Stripe Payment Links verified from rendered checkout

| Intended product | Checkout | Verified checkout display |
|---|---|---|
| CredentialAuditor Pro | https://buy.stripe.com/5kQ14m2DQackeP687L5sA00 | 14 days free, then $99/year |
| PASTE TRAP Standard | https://buy.stripe.com/8x2aEWemyesA9uM4Vz5sA0b | SMB Kit, $499 one time |
| PASTE TRAP Pro | https://buy.stripe.com/28EdR83HU84c6iA2Nr5sA0c | Enterprise Kit, $999 one time |

Do not reuse the CredentialAuditor checkout for ARCANA plans labeled $15/month, $39/month, $49/month, $99/month, $299/year, or $790/year. Those prices do not match the verified Stripe checkout.

## Customer path rules

- Free downloads may link directly to a public release.
- Paid artifacts must not be exposed through an unrestricted pre-payment download link.
- Paid checkout buttons must name the same product and price Stripe displays.
- Post-payment delivery must be configured in Stripe or through an authenticated fulfillment service.
- Production links must use `https://arcana-forensics.com/`, not the retired GitHub Pages marketing URL.

## Revalidation

Recheck this file whenever a Stripe product, price, trial, domain, release, or redirect changes.
