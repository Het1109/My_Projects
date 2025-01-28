# from art import logo
# print(logo)
#
#
# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     winner = ""
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}")
#
#
# bids = {}
# continue_bidding = True
# while continue_bidding:
#     name = input("What is your name?: ")
#     price = int(input("What is your bid?: $"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#     if should_continue == "no":
#         continue_bidding = False
#         find_highest_bidder(bids)
#     elif should_continue == "yes":
#         print("\n" * 20)
from art import logo
import turtle

# Initialize turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("green")  # Set background color to green
screen.title("Auction Bidding")

# Set up turtle for writing
turtle.penup()
turtle.hideturtle()
turtle.color("white")  # Set text color to white

# Display the logo
turtle.goto(0, 150)
turtle.write(logo, align="center", font=("Courier", 12, "normal"))

# Function to find the highest bidder
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    turtle.clear()
    turtle.goto(0, 0)
    turtle.write(f"The winner is {winner} with a bid of ${highest_bid}", align="center", font=("Arial", 16, "bold"))

# Main bidding loop
bids = {}
continue_bidding = True

while continue_bidding:
    # Get user input using turtle
    name = turtle.textinput("Name", "What is your name?: ")
    price = turtle.numinput("Bid", "What is your bid?: $", minval=0)

    # Add bid to the dictionary
    bids[name] = price

    # Ask if there are more bidders
    should_continue = turtle.textinput("Continue", "Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue.lower() == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue.lower() == "yes":
        turtle.clear()  # Clear the screen for the next bidder

# Keep the window open until clicked
turtle.done()