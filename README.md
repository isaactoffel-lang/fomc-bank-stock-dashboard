# FOMC bank-stock dashboard

**Event-study design · Python and Streamlit**

Our DATA Club team studied how bank stocks behaved around changes in monetary policy. I managed the project and led the study design and evaluation work.

The case study starts with when each model input could have been known. A market move after a policy announcement can explain what happened. A forecast made before the announcement cannot use that move.

## Run the review

```sh
python timing_review.py
```

The [runnable example](timing_review.py) uses invented event timelines. It filters out inputs unavailable by the forecast cutoff, accepts a clean chronological holdout, and rejects shared events, reversed chronology, and training outcomes that overlap the holdout. It needs only Python and its standard library.

[Read the methodology and limits](CASE_STUDY.md) · [Publication scope](PUBLICATION.md)

**Original team**  
Isaac Toffel, Alan Chau, Julian Antropow de la Hoz, and Lucas Azout.

The timing review was added with AI assistance for this publication. The original study and its model outputs are separate from this example.
