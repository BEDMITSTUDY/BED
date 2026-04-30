# BED v3 — Synthetic MIT Micro-Pilot Data Dictionary

This document describes the fields in `synthetic_mit_pilot.csv`.

| Field           | Type    | Description |
|-----------------|---------|-------------|
| node_id         | string  | Synthetic MIT location identifier (C1, C2, L1, G1, S1). |
| timestamp       | int     | Simulation timestep. |
| event           | int     | 1 = simulated visit occurred, 0 = no visit. |
| action          | int     | 1 = incentive sent, 0 = no incentive. |
| hazard          | float   | Probability of event (public logistic hazard). |
| recency         | int     | Days since last event. |
| habit           | float   | Habit strength (bounded 0–1). |
| responsiveness  | float   | Responsiveness to incentives (bounded 0–1). |

All values are synthetic and safe for public release.
