#
#Normal code without gui
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#
#     for letter in original_text:
#         if encode_or_decode == "decode":
#             shift_amount *= -1
#
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         output_text += alphabet[shifted_position]
#     print(f"Here is the {encode_or_decode}d result: {output_text}")
#
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
#
#
# caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
#


import turtle
from turtle import Screen

screen = Screen()
screen.tracer(0)

turtle.speed(0)
turtle.hideturtle()
turtle.penup()

title = "Caesar Cipher Encoder/Decoder"
turtle.goto(-200, 150)
turtle.write(title, font=("Arial", 18, "bold"))


def caesar_cipher(text, shift, mode):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""

    if mode == "decode":
        shift *= -1

    for letter in text:
        if letter in alphabet:
            new_pos = (alphabet.index(letter) + shift) % 26
            result += alphabet[new_pos]
        else:
            result += letter
    return result


def encode():
    output.clear()
    message = text_input
    shift = int(shift_input)
    result = caesar_cipher(message.lower(), shift, "encode")
    output.goto(-200, -70)
    output.write(f"Encoded: {result}", font=("Arial", 14, "normal"))


def decode():
    output.clear()
    message = text_input
    shift = int(shift_input)
    result = caesar_cipher(message.lower(), shift, "decode")
    output.goto(-200, -70)
    output.write(f"Decoded: {result}", font=("Arial", 14, "normal"))


# Input fields
turtle.goto(-200, 100)
turtle.write("Enter Text:", font=("Arial", 12, "normal"))
text_input = screen.textinput("Input", "Enter text:")

turtle.goto(-200, 70)
turtle.write("Enter Shift:", font=("Arial", 12, "normal"))
shift_input = screen.numinput("Shift", "Enter shift number:", minval=1, maxval=25)

# Buttons
turtle.goto(-100, 20)
turtle.write("Click below to Encode or Decode", font=("Arial", 12, "normal"))

turtle.goto(-50, -20)
turtle.write("[ Encode ]", font=("Arial", 14, "bold"))

turtle.goto(50, -20)
turtle.write("[ Decode ]", font=("Arial", 14, "bold"))

# Output
output = turtle.Turtle()
output.hideturtle()
output.penup()


def click_handler(x, y):
    if -50 <= x <= 50 and -30 <= y <= -10:
        encode()
    elif 50 <= x <= 150 and -30 <= y <= -10:
        decode()


screen.onclick(click_handler)
screen.mainloop()
