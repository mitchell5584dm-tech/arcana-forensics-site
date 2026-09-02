# Stripe sandbox baseline

Created: 2026-09-01  
Stripe mode: test/sandbox only  
Production impact: none

## Catalog

| Product | Price | Billing |
|---|---:|---|
| CredentialAuditor Pro | $99 USD | Yearly subscription with 14-day trial |
| PASTE TRAP Standard | $499 USD | One time |
| PASTE TRAP Pro | $999 USD | One time |

## Test Payment Links

- CredentialAuditor Pro: https://buy.stripe.com/test_28EbJ05Rs0pOcT3bKwdQQ02
- PASTE TRAP Standard: https://buy.stripe.com/test_5kQcN45Rs6Oc06hbKwdQQ01
- PASTE TRAP Pro: https://buy.stripe.com/test_cNi9ASa7I8Wk4mxg0MdQQ00

## Controls applied

- Products are separate Stripe Products rather than unrelated tiers on one Product.
- Payment methods are dynamic; no hardcoded `payment_method_types`.
- The subscription cancels if the trial ends without a payment method.
- One-time purchases generate invoices.
- Payment Links use Stripe-hosted confirmation rather than exposing paid downloads.
- Automatic tax is disabled because this Stripe account has no recorded tax registrations.
- Metadata distinguishes catalog keys and the sandbox environment.

## Still required for production

1. Connect the live Stripe account.
2. Reconcile or create equivalent live Products, Prices, and Payment Links.
3. Confirm tax registrations before enabling Stripe Tax.
4. Implement signed webhook verification and entitlement-aware fulfillment.
5. Configure the Customer Portal for subscription cancellation and payment-method updates.
6. Test successful, failed, canceled, refunded, and disputed payment paths.
