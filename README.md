# FOMC bank-stock dashboard

An original DATA Club team project exploring the relationship between monetary policy changes and bank-stock behavior.

Original team: Isaac Toffel, Alan Chau, Julian Antropow de la Hoz, and Lucas Azout.

## The research workflow

The original implementation combines an event-study pipeline, feature construction, machine learning models, exploratory analysis, and a Streamlit interface.

| Area | Purpose |
| --- | --- |
| Event pipeline | Relate policy changes to market observations |
| Feature construction | Prepare explanatory inputs |
| Modeling | Explore relationships between inputs and outcomes |
| Dashboard | Make the research workflow inspectable |

## Methodology limits

The event construction derives policy changes from the rate series and does not include every policy meeting. Trading-day windows need careful interpretation. Shuffled validation can leak information across related observations. Features measured after an announcement cannot establish a prediction made before that announcement.

The project is exploratory research. This writeup makes no performance, forecasting, or trading-profit claim.

## Public scope

This public repository contains a qualitative project writeup only. Original source, notebooks, chart outputs, development history, and attribution records are retained privately. This repository provides no runnable application, financial results, contact information, or live data connection.

AI assisted with additional checks and documentation. Publishing this writeup does not revalidate the original live application.
