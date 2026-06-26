# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

Implement Challenge 4: Enhanced Game UI by adding:
1. Color-coded hints using Streamlit markdown formatting
2. Hot/Cold emoji indicators based on distance from the secret number
3. A real-time summary table showing all guesses with distance and outcome
4. Improved game end messages with emphasis
5. All without breaking the core game logic in `logic_utils.py`

**What did the agent do?**

1. Added session state tracking for detailed guess history (`detailed_history` list)
2. Modified the "New Game" button to properly reset all state variables (attempts, score, history, detailed_history)
3. Updated guess submission logic to:
   - Calculate absolute distance from secret number
   - Determine Hot/Cold status based on distance thresholds
   - Store detailed history as dictionaries with Attempt, Guess, Distance, Status, Outcome
4. Enhanced hint display with:
   - Markdown bold formatting for emphasis
   - Color-coded messages (success for Win, warning for Too High/Too Low)
   - Hot/Cold emoji indicators inline with hints
5. Added Pandas DataFrame table display for guess history
6. Improved game end messages with larger emphasis
7. Added `pandas` to requirements.txt
8. Added pandas import at top of app.py

**What did you have to verify or fix manually?**

1. Verified that all pytest tests still pass (4/4 passing) — no logic changes broke existing tests
2. Checked syntax validation of modified app.py with `py_compile` — valid
3. Confirmed the Hot/Cold distance thresholds made sense (5, 10, 20, 50 ranges)
4. Ensured pandas import was at module top-level, not inline
5. Verified that the detailed_history DataFrame displayed correctly by reviewing the code
6. Double-checked that New Game button reset all necessary state variables

All changes were correct on first attempt — no manual fixes needed!

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
