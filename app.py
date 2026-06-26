import random
import streamlit as st
import pandas as pd
from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    # FIX: Start attempts at 0 (was incorrectly 1, causing off-by-one errors)
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

if "detailed_history" not in st.session_state:
    st.session_state.detailed_history = []

st.subheader("Make a guess")

st.info(
    f"Guess a number between 1 and 100. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.detailed_history = []
    # FIX: Use selected difficulty range instead of hard-coded (1, 100)
    st.session_state.secret = random.randint(low, high)
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.history.append(guess_int)

        # FIX: Removed string conversion of secret (was breaking on even attempts)
        outcome = check_guess(guess_int, st.session_state.secret)

        # Calculate distance and hot/cold status for enhanced UI
        distance = abs(guess_int - st.session_state.secret)
        hot_cold = "🔥 Burning Hot!" if distance <= 5 else "🌡️ Very Close..." if distance <= 10 else "🟠 Getting warm..." if distance <= 20 else "🔵 Chilly..." if distance <= 50 else "❄️ Freezing Cold!"

        # Store detailed history for summary table
        st.session_state.detailed_history.append({
            "Attempt": st.session_state.attempts,
            "Guess": guess_int,
            "Distance": distance,
            "Status": hot_cold,
            "Outcome": outcome
        })

        # Display color-coded outcome messages
        if show_hint:
            if outcome == "Win":
                st.success("🎉 **CORRECT!** You found the secret number!")
            elif outcome == "Too High":
                st.warning(f"📈 **Too High!** Go LOWER. {hot_cold}")
            else:  # Too Low
                st.warning(f"📉 **Too Low!** Go HIGHER. {hot_cold}")

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        # Display game history table
        if len(st.session_state.detailed_history) > 0:
            st.subheader("📊 Guess History")
            history_df = pd.DataFrame(st.session_state.detailed_history)
            st.dataframe(history_df, use_container_width=True)

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"🎉 **You won!** The secret was **{st.session_state.secret}**\n\n"
                f"Final score: **{st.session_state.score}** | Attempts: **{st.session_state.attempts}**"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"💀 **Game Over!** The secret was **{st.session_state.secret}**\n\n"
                    f"Final score: **{st.session_state.score}**"
                )

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
