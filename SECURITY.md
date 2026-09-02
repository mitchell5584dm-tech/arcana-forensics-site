# Security Policy

## Supported surface

Security fixes are provided for the current production website at https://arcana-forensics.com/ and the latest published release referenced by that site. Older prototypes, duplicate case-variant HTML files, and historical downloads are unsupported unless explicitly identified in a release note.

## Reporting a vulnerability

Please report vulnerabilities privately through GitHub's private vulnerability reporting feature for this repository. If that feature is unavailable, contact the repository owner through the GitHub profile without posting exploit details publicly.

Include:

- affected URL, file, or release;
- reproduction steps and impact;
- browser/OS or runtime details;
- a minimal proof of concept with sensitive data removed.

Do not include customer data, credentials, payment information, or live secrets. Please allow a reasonable period for triage and remediation before public disclosure.

## Scope and safe research

Good-faith testing must avoid service disruption, social engineering, accessing other people's data, purchases, or destructive actions. Stripe processes payments; this repository must never contain Stripe secret keys or card data.
