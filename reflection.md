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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
