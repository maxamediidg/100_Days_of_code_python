import  turtle
import  pandas

screen = turtle.Screen()
screen.title("U.S state Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_sates = []

while len(guess_sates) < 50:
	answer_state = screen.textinput(title=f"{len(guess_sates)}/50 states Correct",
									prompt="what's another state's name?r").title()

	if answer_state == "Exit":
		missing_states = []
		for state in all_states:
			if state not in guess_sates:
				missing_states.append(state)
		new_data = pandas.DataFrame(missing_states)
		new_data.to_csv("states_to_learn.csv")
		break

	if answer_state in all_states:
		guess_sates.append(answer_state)
		t = turtle.Turtle()
		t.hideturtle()
		t.penup()
		state_data = data[data.state == answer_state]
		t.goto(int(state_data.x), int(state_data.y))
		t.write(answer_state)


# state to learn.csv
