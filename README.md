# Toxicity Strategy

Inspired by the album Toxicity

## Behavior Summary

- **Start cooperatively**, assuming goodwill.
- **Detects toxicity** early: if the opponent defects 3 or more times in the first 5 rounds, they are marked as "toxic".
- Against **toxic opponents**:
  - Follows a chaotic retaliation pattern.
  - Betrays on Fibonacci-numbered rounds.
  - Occasionally mirrors the opponent’s betrayal.
  - Escalates into full defection mode after round 51 (album duration).
- Against **non-toxic opponents**:
  - Plays a gentle **tit-for-tat**.
  - Forgives betrayals every 7 rounds.

    
---

