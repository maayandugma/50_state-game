import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_atate = screen.textinput(title=f"{len(guessed_state)/50}Guess the state",
                                    prompt="What's another state's name?").title() #the first letter need to be big
    if answer_atate == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        break
    if answer_atate in all_states:
        guessed_state.append(answer_atate)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_atate] #get the specific state
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_atate)


screen.exitonclick()