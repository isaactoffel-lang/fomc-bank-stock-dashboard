"""Executable review of event-study timing using invented observations."""

from dataclasses import dataclass
from enum import IntEnum, auto


class Moment(IntEnum):
    EARLY_CUTOFF = auto()
    EARLY_ANNOUNCEMENT = auto()
    EARLY_OUTCOME = auto()
    LATE_CUTOFF = auto()
    LATE_ANNOUNCEMENT = auto()
    LATE_OUTCOME = auto()


@dataclass(frozen=True)
class Observation:
    event: str
    forecast_cutoff: Moment
    announcement: Moment
    outcome_available: Moment


@dataclass(frozen=True)
class Feature:
    name: str
    available: Moment


def forecast_inputs(observation, features):
    """Select inputs observable by the pre-announcement decision cutoff."""
    if observation.forecast_cutoff >= observation.announcement:
        raise ValueError("Forecast cutoff must precede the announcement")
    return tuple(
        feature.name
        for feature in features
        if feature.available <= observation.forecast_cutoff
    )


def validate_holdout(training, holdout):
    """Check event separation and whether training labels were known in time."""
    if not training or not holdout:
        raise ValueError("Training and holdout both need observations")

    for row in (*training, *holdout):
        if not row.forecast_cutoff < row.announcement <= row.outcome_available:
            raise ValueError("An observation has an invalid timeline")

    if {row.event for row in training} & {row.event for row in holdout}:
        raise ValueError("An event appears on both sides of the split")

    earliest_holdout_cutoff = min(row.forecast_cutoff for row in holdout)
    if any(row.outcome_available >= earliest_holdout_cutoff for row in training):
        raise ValueError("A training outcome is unavailable before holdout begins")


def expect_rejected(training, holdout, reason):
    try:
        validate_holdout(training, holdout)
    except ValueError as error:
        if reason not in str(error):
            raise
        print(f"PASS | Rejected: {error}")
    else:
        raise AssertionError(f"Expected rejection: {reason}")


def main():
    early = Observation(
        "early meeting", Moment.EARLY_CUTOFF,
        Moment.EARLY_ANNOUNCEMENT, Moment.EARLY_OUTCOME,
    )
    late = Observation(
        "late meeting", Moment.LATE_CUTOFF,
        Moment.LATE_ANNOUNCEMENT, Moment.LATE_OUTCOME,
    )
    overlapping = Observation(
        "overlapping window", Moment.EARLY_CUTOFF,
        Moment.EARLY_ANNOUNCEMENT, Moment.LATE_OUTCOME,
    )
    features = (
        Feature("prior-session trend", Moment.EARLY_CUTOFF),
        Feature("policy surprise", Moment.EARLY_ANNOUNCEMENT),
        Feature("market response", Moment.EARLY_OUTCOME),
    )

    if forecast_inputs(early, features) != ("prior-session trend",):
        raise AssertionError("Unexpected feature availability")
    print("PASS | Kept pre-announcement input and excluded later observations")
    validate_holdout((early,), (late,))
    print("PASS | Accepted a chronological split with separate events")
    expect_rejected((early,), (early, late), "both sides")
    expect_rejected((overlapping,), (late,), "unavailable")
    expect_rejected((late,), (early,), "unavailable")


if __name__ == "__main__":
    main()
