# BED v3 Prototype

This folder contains the minimal working prototype for the BED closed-loop incentive system.

Components:
- static_page.html — QR-triggered landing page
- cloud_function.js — serverless backend that assigns incentives and logs events
- firestore_schema.json — synthetic schema for event logging

This prototype is intentionally lightweight and MIT-safe:
- No PII collected
- No POS integration
- Serverless backend
- Firestore logging
