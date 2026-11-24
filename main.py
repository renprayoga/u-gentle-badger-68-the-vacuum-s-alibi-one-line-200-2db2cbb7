"""The Vacuum's Alibi — one-line excuse entry (make.fun).

Strategy report (Protokol Top 5 — laporan sebelum kode akhir):

Entry line (119 characters, one line):
    Spot report: dust located, identified as a crumb from your 2 a.m. snack,
    left as evidence. I do not clean crime scenes.

Why this line wins against the judge rubric (most important first):
1. Funny one-line excuse for a missed spot — it IS the vacuum's excuse:
   the spot was not missed by accident, it was deliberately left behind.
2. Real laugh, joke that lands — the turn is a crime-scene frame: the dust
   is "evidence" and the vacuum refuses to clean a crime scene. The joke
   reframes laziness as forensic procedure, not a cute observation about dust.
3. Deadpan robot voice — opens with a machine-style "Spot report:", speaks
   in flat bureaucratic verbs (located, identified, left), and stays smug
   about its own sensors doing the identifying.
4. Surprise, specific detail nobody expects — "a crumb from your 2 a.m.
   snack" is a concrete, slightly incriminating detail (the owner was
   snacking at 2 a.m.); nobody expects the vacuum to know that, or to use
   it as an alibi.
5. Tightness, punch at the end — 119 of 200 characters, every word earns
   its place; the punch ("I do not clean crime scenes.") is the last
   sentence, so the laugh lands on the final beat.

Candidates considered and rejected:
- A (143 chars): "...classified it as the dog's problem now... clear
  conscience." — the dog joke is a stock appliance gag, and the punch
  ("clear conscience") is soft; it explains the miss instead of
  reframing it.
- B (120 chars): "...filed it under 'not my department,' and my battery
  signed off..." — bureaucratic and deadpan, but the punch is a shrug;
  no surprise detail, no laugh that lands.

Optimisation: the line is a compile-time constant — O(1) time, O(1)
memory, zero input, zero network, zero randomness, fully deterministic.
Edge cases: the gate requires 1–200 characters, one line, not only
whitespace. main() validates all three before writing and refuses to
write an invalid line, so a bad constant can never reach the judge.
"""

import os
import sys

LINE = (
    "Spot report: dust located, identified as a crumb from your "
    "2 a.m. snack, left as evidence. I do not clean crime scenes."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce the gate: 1 line, 1-200 chars, not only whitespace."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(f"wrote {len(LINE)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
