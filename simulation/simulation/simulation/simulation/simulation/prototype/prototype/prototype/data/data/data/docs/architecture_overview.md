# BED v3 — System Architecture Overview

This document provides a high-level overview of the BED v3 architecture,
including the simulation engine, CMDP policy layer, prototype pipeline, and
data flow.

## 1. Simulation Architecture

The simulation engine consists of:
- Behavioral state model (recency, habit, responsiveness)
- Logistic hazard model
- CMDP policy module
- Simulation runner and configuration

The simulation produces synthetic event logs used for analysis and validation.

## 2. Prototype Architecture

The minimal working prototype includes:
- QR-triggered static web page
- Cloud Function backend
- Firestore event logging
- Synthetic schema for safe public release

This prototype demonstrates the closed-loop flow without exposing production
logic or private integrations.

## 3. Data Flow

1. User scans QR → static page loads  
2. Page sends event → Cloud Function  
3. Cloud Function logs event → Firestore  
4. Data exported → analysis notebooks  
5. Simulation + prototype data → unified evaluation  

## 4. Privacy and Safety

All real-world data, tuning parameters, and production integrations are excluded
from this repository (see NOTICE).
