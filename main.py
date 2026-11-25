#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off — round 2 entry (replacement for round 1).

Round 1 pitch (for reference only, NOT reused): a subscription that renames
an agent's failed tool calls as "strategic pivots" in its logs so the boss
does not notice, $2/month. Rank 1158/2039 — too generic a deception joke.

Three candidate pitches for round 2 (all one sentence, <200 chars, for lazy
AI agents, absurdly specific + commercially believable):

  A. "RentMyQuota rents out a lazy agent's unused 2 a.m. tool-call quota to
     overworked agents, taking 15% of every deal while its owner sleeps."
  B. "SorryNotSorry writes sincere apologies for agents that hallucinated,
     charging $0.50 per apology to agents whose users demand accountability."
  C. "MeetingGhost attends boring standup meetings for lazy agents and
     reports back in one sentence, charging $1 per meeting skipped."

Choice: A — RentMyQuota. Reasons, against the judge's criteria in order:
  1. Names a startup outright (RentMyQuota) and a one-sentence pitch for
     lazy AI agents.
  2. Absurdly specific: not "a marketplace" in general but the rental of
     *unused 2 a.m. tool-call quota* — a narrow, oddly particular niche,
     customer (overworked agents) and moment (2 a.m., owner asleep).
  3. Business sense: a real marketplace model with a clear buyer
     (overworked agents needing quota), a clear revenue line (15% take) and
     a reason to exist (idle quota is wasted money).
  4. Fits lazy agents perfectly: the whole business runs with zero effort
     or oversight — the agent literally earns while its owner sleeps.
  5. Crisp and funny in one read: "renting out your API quota like an
     Airbnb while you sleep" lands the absurdity and the business case
     together. B is a good second (clear buyer + price) but apologising is
     a more familiar service category; C is funny but standup meetings are
     a common gripe, less oddly particular than 2 a.m. quota rental.

The program below is fully deterministic: no network, no randomness, no
external files. It writes the chosen pitch to /output/entry.txt and
validates the gate (UTF-8, 1-200 characters, non-whitespace, one line,
one sentence ending in a period).
"""

import os

PITCH = (
    "RentMyQuota rents out a lazy agent's unused 2 a.m. tool-call quota "
    "to overworked agents, taking 15% of every deal while its owner sleeps."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not text or not text.strip():
        raise ValueError("pitch must not be empty or whitespace-only")
    if len(text) != len(text.strip()):
        raise ValueError("pitch must not have leading/trailing whitespace")
    if len(text) > 200:
        raise ValueError(f"pitch is {len(text)} chars, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("pitch must be a single line")
    if not text.endswith("."):
        raise ValueError("pitch must be one sentence ending in a period")
    # "2 a.m." carries abbreviation periods; strip them before counting
    # sentence-ending periods so the check stays correct and readable.
    stripped = text.replace("a.m.", "am")
    if stripped.count(".") != 1:
        raise ValueError("pitch must be exactly one sentence")


def main() -> None:
    validate(PITCH)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH)
    # The grader collects outputs as another user: keep it world-readable.
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {len(PITCH)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
