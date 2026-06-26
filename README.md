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

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
