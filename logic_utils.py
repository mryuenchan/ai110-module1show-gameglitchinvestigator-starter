def get_range_for_difficulty(difficulty: str):
    """Return the inclusive number range for the selected difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50

    return 1, 100


def parse_guess(raw: str):
    """Turn user input into an integer guess."""
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        value = int(raw)
    except ValueError:
        return False, None, "That is not a whole number."

    return True, value, None


def check_guess(guess: int, secret: int):
    """Compare a guess with the secret and return an outcome and hint."""
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!" #FIX: When its too high, hint should be "Go LOWER!" instead of "Go HIGHER!"

    return "Too Low", "📈 Go HIGHER!" #FIX: When its too low, hint should be "Go HIGHER!" instead of "Go LOWER!"

def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update the score based on the guess result."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)

        if points < 10:
            points = 10

        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


def get_attempts_left(attempts: int, attempt_limit: int):
    """Return remaining attempts without allowing a negative value."""
    return max(0, attempt_limit - attempts)

