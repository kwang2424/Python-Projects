import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'us-states-game/us-states-game-start/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.penup()
writer.ht()

states_data = pandas.read_csv('us-states-game\\us-states-game-start\\50_states.csv')

states = 0
state_list = states_data['state'].to_list()
while states < 50:
    answer_state = screen.textinput(title=f"Guess the State {states}/50", prompt="What's the state's name?").title()
    if answer_state in state_list:
        x = states_data[states_data.state == answer_state]
        x = x.x
        x = int(x)
        y = states_data[states_data.state == answer_state]
        y = y.y
        y = int(y)
        writer.goto(x, y)
        writer.write(answer_state)
        state_list.remove(answer_state)
        states += 1
    if answer_state == 'Exit':
        states_to_learn = pandas.DataFrame(state_list)
        states_to_learn.to_csv('states_to_learn.csv')
        break
