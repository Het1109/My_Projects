# # Display art
# from art import logo, vs
# from game_data import data
# import random
#
#
# def format_data(account):
#     """Takes the account data and returns the printable format."""
#     account_name = account["name"]
#     account_descr = account["description"]
#     account_country = account["country"]
#     return f"{account_name}, a {account_descr}, from {account_country}"
#
#
# def check_answer(a_followers, b_followers):
#     """Take a user's guess and the follower counts and returns if they got it right."""
#     if a_followers > b_followers:
#         return guess == "a"
#     else:
#         return guess == "b"
#
#
# print(logo)
# score = 0
# game_should_continue = True
# # Generate a random account from the game data
# account_b = random.choice(data)
#
# # Make the game repeatable.
# while game_should_continue:
#
#     # Making account at position B become the next account at position A.
#     account_a = account_b
#     account_b = random.choice(data)
#
#     if account_a == account_b:
#         account_b = random.choice(data)
#
#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}.")
#
#     # Ask user for a guess.
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#
#     # Clear the screen
#     print("\n" * 20)
#     print(logo)
#
#     # - Get follower count of each account
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#
#     # Check if user is correct.
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)
#
#     # Give user feedback on their guess.
#     # score keeping.
#     if is_correct:
#         score += 1
#         print(f"You're right! Current score {score}")
#     else:
#         print(f"Sorry, that's wrong. Final score: {score}.")
#         game_should_continue = False
#
#
import turtle
import random
from game_data import data

# Set up the screen
turtle.setup(width=800, height=600)
turtle.bgcolor("white")
turtle.title("Who Has More Followers?")

# Create turtle objects
screen = turtle.Screen()
screen.tracer(0)
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed(0)


def draw_text(text, x, y, size=20, color="black"):
    """Helper function to draw text on the screen."""
    t.goto(x, y)
    t.color(color)
    t.write(text, align="center", font=("Arial", size, "bold"))


def format_data(account):
    """Formats account data into a readable format."""
    return f"{account['name']} \n{account['description']} from {account['country']}"


def draw_screen(account_a, account_b, score):
    """Draws the game screen with the two accounts."""
    t.clear()
    draw_text(f"Score: {score}", 0, 250, 24, "blue")

    draw_text("🌟 Compare A:", -200, 100, 20, "red")
    draw_text(format_data(account_a), -200, 50, 16)

    draw_text("VS", 0, 0, 30, "purple")

    draw_text("⚡ Against B:", 200, 100, 20, "green")
    draw_text(format_data(account_b), 200, 50, 16)

    draw_text("Press 'A' or 'B' to choose!", 0, -200, 18, "black")
    screen.update()


def check_answer(guess, account_a, account_b):
    """Checks if the guess is correct and updates the game accordingly."""
    global score, game_should_continue, account_b_data
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    is_correct = (guess == "a" and a_followers > b_followers) or (guess == "b" and b_followers > a_followers)

    if is_correct:
        score += 1
        draw_text("✅ Correct!", 0, -100, 20, "green")
        account_a_data = account_b_data  # Move B to A
        account_b_data = random.choice(data)
        draw_screen(account_a_data, account_b_data, score)
    else:
        draw_text(f"❌ Game Over! Final Score: {score}", 0, -100, 20, "red")
        game_should_continue = False
        screen.update()


# Initialize game variables
score = 0
game_should_continue = True
account_a_data = random.choice(data)
account_b_data = random.choice(data)
if account_a_data == account_b_data:
    account_b_data = random.choice(data)

draw_screen(account_a_data, account_b_data, score)

# Key bindings
screen.listen()
screen.onkey(lambda: check_answer("a", account_a_data, account_b_data), "a")
screen.onkey(lambda: check_answer("b", account_a_data, account_b_data), "b")

screen.mainloop()
