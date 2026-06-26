# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Purpose:** A number-guessing game built with Streamlit where players try to guess a secret number within a difficulty-based range. The AI-generated starter code had multiple critical bugs that made it unplayable.

**Bugs Found:**
1. Hint messages were inverted: "Too High" displayed "Go HIGHER!" and "Too Low" showed "Go LOWER!" 
2. Even-numbered attempts converted the secret number to a string, breaking the equality check and making the game unwinnable on even turns
3. The attempts counter started at 1 instead of 0, causing off-by-one errors in scoring and display calculations
4. The "New Game" button hard-coded the range to (1, 100) instead of respecting the selected difficulty level
5. The Hard difficulty range was (1, 50) — narrower than Normal's (1, 100) — making it easier instead of harder

**Fixes Applied:**
- Refactored all game logic functions into `logic_utils.py` with correct implementations
- Updated `app.py` to import and use these functions, removing inline definitions
- Corrected hint messages to properly guide players (Too High → "Go LOWER!", Too Low → "Go HIGHER!")
- Fixed attempts initialization from 1 to 0
- Updated New Game button to use the selected difficulty's range
- Removed string conversion of the secret number
- Fixed Hard difficulty range to (1, 200)
- Added pytest regression tests to prevent hint-inversion bugs from recurring

## 📸 Demo Walkthrough

A sample game session with difficulty set to "Normal":

1. **Start Game:** User opens app, selects "Normal" difficulty (range 1-100), secret is generated and hidden
2. **First Guess:** User enters 50 → Game shows "📈 Go LOWER!" (guess was too high; secret was 35)
3. **Second Guess:** User enters 25 → Game shows "📉 Go HIGHER!" (guess was too low; secret was 35)
4. **Third Guess:** User enters 35 → Game displays "🎉 Correct!" with balloons and final score
5. **Score Calculation:** Score updates based on number of attempts; fewer attempts = higher score
6. **New Game Option:** Player can click "New Game 🔁" to start fresh with a new secret number

## 🧪 Test Results

```
============================= test session starts ==============================
collected 4 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 25%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 50%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 75%]
tests/test_game_logic.py::test_high_guess_returns_correct_outcome PASSED [100%]

============================== 4 passed in 0.02s =========================
```

## 🚀 Stretch Features

### Challenge 4: Enhanced Game UI ✅

**Enhancements Implemented:**

1. **Color-Coded Hints with Markdown Formatting**
   - "Correct!" displays in green with emoji 🎉
   - "Too High" displays in orange/warning style with emoji 📈
   - "Too Low" displays in orange/warning style with emoji 📉
   - All hint text uses bold formatting for emphasis
   - Modified in `app.py` (lines 117-122)

2. **Hot/Cold Emoji System Based on Distance**
   - **🔥 Burning Hot!** — Distance ≤ 5 (extremely close)
   - **🌡️ Very Close...** — Distance ≤ 10 (very close)
   - **🟠 Getting warm...** — Distance ≤ 20 (getting closer)
   - **🔵 Chilly...** — Distance ≤ 50 (far away)
   - **❄️ Freezing Cold!** — Distance > 50 (very far)
   - Calculated dynamically on each guess in `app.py` (line 114)
   - Displayed inline with guess hints (lines 119-122)

3. **Guess History Summary Table**
   - Real-time table showing all guesses with:
     - **Attempt:** Guess number
     - **Guess:** The number the player guessed
     - **Distance:** Absolute distance from secret number
     - **Status:** Hot/Cold emoji indicator
     - **Outcome:** Whether it was "Win", "Too High", or "Too Low"
   - Displayed after each guess using Pandas DataFrame (lines 124-127)
   - Provides players with a clear, text-based record of their game progression

4. **Improved Game End Messages**
   - Win state: Displays secret number and final score with emphasis
   - Lose state: Clear communication with secret reveal
   - Modified in `app.py` (lines 129-140)

5. **Session Reset on New Game**
   - All state variables properly reset: attempts, score, history, detailed_history
   - Prevents carryover from previous games
   - Modified in `app.py` (lines 75-81)

**Dependencies Added:**
- `pandas` — for creating and displaying the guess history DataFrame

**Core Logic Unchanged:**
- All functions in `logic_utils.py` remain untouched
- Game logic (checking guesses, scoring) is identical
- UI enhancements are purely presentational
