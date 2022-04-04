import pandas
from turtle import Screen, Turtle
from tkinter import messagebox

BACKGROUND_IMAGE = "blank_states_img.gif"
STATE_FONT = ("Arial", 8, "normal")
screen = Screen()
screen.setup(width=725, height=491)
screen.bgpic(BACKGROUND_IMAGE)

printer = Turtle()
printer.hideturtle()
printer.penup()

states_data = pandas.read_csv("50_states.csv")

states_guessed = []

while len(states_guessed) < 50:

	user_input = screen.textinput(title=f"Guessed: {len(states_guessed)} of 50", prompt="Enter a name of the state:")

	if user_input.title() in states_guessed:
		while user_input.title() in states_guessed:
			user_input = screen.textinput(title=f"Guessed: {len(states_guessed)} of 50",
										  prompt="You already guessed this one. Try another one!")

	if user_input.title() in states_data["state"].to_list():
		xcor = int(states_data[states_data.state == user_input.title()]["x"])
		ycor = int(states_data[states_data.state == user_input.title()]["y"])
		printer.goto(x=xcor, y=ycor)
		printer.write(user_input.title(), align="center", font=STATE_FONT)
		states_guessed.append(user_input.title())

messagebox.showinfo(title="You win!!!",
					message="Congratulations!\n"
							"You've guessed all 50 states!")