# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first examined the code, I found multiple critical bugs that made the game unplayable. The most impactful were: (1) the hint messages were backwards — "Too High" instructed players to "Go HIGHER!" when they should go lower, (2) even-numbered guess attempts converted the secret number to a string, breaking the equality check and making the game unwinnable on those turns, and (3) the attempts counter started at 1 instead of 0, causing off-by-one errors in scoring and attempt-limit display. A fourth bug affected difficulty selection: the "New Game" button ignored the selected difficulty and always reset the range to (1, 100). These issues combined made the game essentially non-functional.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 60 (secret 50) | "Too High" hint, "Go LOWER!" message | "Too High" hint, "Go HIGHER!" message shown | none |
| Guess 40 (secret 50) | "Too Low" hint, "Go HIGHER!" message | "Too Low" hint, "Go LOWER!" message shown | none |
| Attempt #2 with guess 50 (secret 50) | Score updates, game ends with "Win" | String/int comparison breaks; hint becomes unintelligible | TypeError or incorrect hint |
| Attempt #4 with guess 75 (secret 75) | Win on even attempt | String/int mismatch prevents correct detection | TypeError or false negative |
| Select "Hard" difficulty, start game | Secret range should be (1, 200) | Secret range is (1, 100) — same as Normal difficulty | none |

---

## 2. How did you use AI as a teammate?

I used Claude as my AI assistant, integrated into VS Code, to understand bugs, refactor code, and generate test cases. The AI workspace integration let me highlight specific code sections and ask clarifying questions about logic flow.

**Correct Suggestion:** The AI correctly identified that `check_guess()` should return just the outcome string ("Win", "Too High", "Too Low") rather than a tuple of (outcome, message). This made the function reusable and testable. I verified this was correct by writing tests that asserted on the outcome string directly, and all 4 pytest tests passed.

**Misleading Suggestion:** Initially, the AI suggested keeping the tuple return format (outcome, message) in `check_guess()` to avoid redundant message logic in app.py. However, I recognized this violated the separation-of-concerns principle — UI presentation (emoji messages) shouldn't live in game logic. The AI's suggestion was well-intentioned but architecturally wrong. I corrected it by moving the messages into app.py's display logic and updating the tests accordingly.

---

## 3. Debugging and testing your fixes

To verify each bug was truly fixed, I used a two-pronged approach: automated pytest tests for logic functions, and manual gameplay testing via `streamlit run app.py` for UI state. For the hint-inversion bug, I ran `pytest test_game_logic.py::test_guess_too_high` and confirmed it returned "Too High" for a guess of 60 against secret 50 — exactly the outcome we expect.

For the attempts counter bug, I ran a full game where I checked the "Developer Debug Info" expander to watch the attempts value increment from 0 correctly. The score also updated properly based on attempt number (fewer attempts = higher score), confirming the off-by-one fix was complete.

The AI helped me design the `test_high_guess_returns_correct_outcome()` test by suggesting I add a regression test targeting the specific inversion bug. This test catches if someone accidentally re-inverts the logic in the future. Running `pytest` showed all 4 tests passing, which gave me confidence the game logic was sound end-to-end.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns are different from traditional web frameworks: **every time a user interacts with a widget (button, text input, slider), Streamlit re-executes the entire script from top to bottom.** This was shocking at first—normally you'd expect just that one interaction to process. But it means Streamlit scripts are much simpler to reason about.

To keep data across reruns (like game state: secret number, attempts, score), you use `st.session_state`, a special dictionary that persists across reruns. Without session state, the secret would reset on every button click. The key insight: **Streamlit reruns are a feature, not a bug**—they keep your code linear and easy to follow, and session_state handles persistence. This project taught me that bad state management (like attempts starting at 1 instead of 0, or the New Game button resetting to hard-coded values) cascades through the entire game experience. Careful initialization of session_state is critical.

---

## 5. Looking ahead: your developer habits

**Habit to reuse:** Adding regression tests for newly fixed bugs. When I found that hints were inverted, I added `test_high_guess_returns_correct_outcome()` to catch any future re-inversion. This habit of "test what you fix" prevents bugs from silently creeping back in during refactors. I'll apply this to all future bug fixes.

**What I'd do differently:** I'd ask the AI to explain *why* it chose a particular architecture (like return types) rather than just accepting its first suggestion. The AI is a great partner for explaining trade-offs, and understanding the reasoning upfront saves iteration cycles later.

**How this changed my thinking:** AI-generated code is not "production-ready" by default — it's a starting point that needs critical review. This project showed me that even simple logic can have subtle bugs, and shipping AI code without testing it live is dangerous. The quality gate isn't whether the AI wrote it, but whether I verified it end-to-end (tests + manual play-through).
