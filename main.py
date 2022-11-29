import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct = 0
game_is_on = True




while game_is_on:
    answer_state = screen.textinput(title=f'Correct states: 50/{correct}', prompt="'What's another state's name? ").capitalize()
    data = pandas.read_csv('50_states.csv')
    state = data.state
    comparing = data[state == answer_state]
    comparing_x = int(comparing.x)
    comparing_y = int(comparing.y)

    for s in state:
        if s == answer_state:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(x=comparing_x, y=comparing_y)
            comparing_state = comparing.state
            for state in comparing_state:
                t.write(state)
            correct += 1
            t.goto(0, 0)



screen.exitonclick()
