# The timestamp sets the claim

[Project overview and credits](README.md) · [Timing review source](timing_review.py)

## Define the event before choosing the model

The DATA Club project derived events from changes in a policy rate series and aligned them with trading-day observations. That gave the team a concrete event definition. It also restricted the sample to policy rate changes. A meeting that left the rate unchanged could still move the market, so the results describe a narrower population than all policy meetings.

A trading window introduces another decision. A response can be measured only once the observations that define it are available. Market session boundaries and release times therefore matter even when all records use the same calendar date.

## Separate explanation from prediction

| Information | Pre-announcement forecast | Event description |
| --- | --- | --- |
| Prior-session trend | Available if observed by the cutoff | Available |
| Policy surprise | Available after the announcement | Can help characterize the event |
| Market response | Future outcome at the cutoff | Measures the subsequent move |

A model can appear to anticipate the market if the response leaks into the inputs. Even with valid inputs, a shuffled row split can put bank observations from the same meeting into both training and evaluation. A split by event addresses that dependency. Chronology adds a separate check that the training outcomes were already observable at the first holdout cutoff.

## What the public example verifies

The [timing review](timing_review.py) uses symbolic timestamps to show the forecast boundary and both split checks. It includes a case where the event groups are different but the training label arrives too late. That case would pass a group-only split.

The example runs on invented observations. Establishing predictive performance would require point-in-time market data, a full meeting calendar for claims about all meetings, and an evaluation against a baseline using the same horizon. The public example verifies the rules it implements. [Publication scope](PUBLICATION.md)
