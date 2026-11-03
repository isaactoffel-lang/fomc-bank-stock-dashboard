# FOMC dashboard case study

[Project overview](README.md) · [Publication scope](PUBLICATION.md)

## The timestamp sets the claim

Research can describe a relationship without establishing that the relationship could have been used in advance. For an event study, the timing of the event, the observation window, and the feature all affect the conclusion.

The FOMC bank-stock dashboard is an original DATA Club team project that combines an event-study pipeline, features, exploratory models, and a Streamlit interface. This case study explains that chain and the limitations already identified in its methodology.

## Event construction

The implementation derives change events from a policy rate series. That is a concrete event definition, but it is narrower than a calendar of all policy meetings.

The distinction changes the population being studied. A meeting without a rate change is not represented by the same construction. Describing the resulting dataset as every policy meeting would therefore imply coverage the method does not provide.

Trading-day windows introduce another interpretation boundary. A market observation window needs to be explained in terms of the trading calendar rather than assumed to match ordinary calendar spacing.

## Feature availability

Feature construction turns observations into inputs for analysis. The relevant question is not only what an input measures, but when that measurement would have been available.

A feature measured after an announcement may be useful for describing the observed response. It cannot establish a prediction made before the announcement. The analysis needs to preserve that distinction in both its evaluation and the language used to present it.

| Layer | Question a reviewer should ask |
| --- | --- |
| Event definition | What qualifies as an event, and which meetings are omitted? |
| Observation window | How is the trading calendar handled? |
| Feature construction | When would this input have become available? |
| Evaluation | Can related observations appear on both sides of a split? |
| Presentation | Does the stated conclusion match the information actually available? |

## Evaluation leakage

Shuffled validation can place related observations into different parts of an evaluation. That separation may look independent while still allowing information about the same event or nearby period to cross the boundary.

Grouping related observations and respecting chronology would strengthen the evaluation design. Those are review directions, not claims that a new grouped or chronological evaluation has been implemented during this publication pass.

The same discipline applies to a dashboard. A clear display makes an analysis easier to examine, but presentation cannot repair an evaluation that answers a different question from the one claimed.

## Engineering responsibilities

The project separates event construction, feature preparation, exploratory modeling, and presentation. That structure gives reviewers distinct places to examine a coverage issue, a timing issue, a modeling choice, or a misleading explanation.

The Streamlit interface is the presentation layer of the original research workflow. The public case study documents that responsibility without presenting a live deployment or model output as current evidence.

## Attribution and evidence

The original team is credited in the [project overview](README.md). AI assisted with additional checks and documentation, rather than replacing the original team's attribution.

This editorial review checks the public explanation and publication boundaries. It does not rerun the original research pipeline or establish predictive performance.

Source, notebooks, chart outputs, license records, and development history are retained privately. The public repository makes no trading-profit or investment-performance claim.
