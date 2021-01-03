import turtle
import pandas as pd



screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Get coordinates
# def get_mouse_click_cor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_cor)


# data
data = pd.read_csv('50_states.csv')


# state
state = list(data['state'])


# coordinates
coordinates = list(zip(data['x'], data['y']))


# write to screen
writer = turtle.Turtle(shape='circle')


answer_state = screen.textinput(title=f"/50 Guess the State", prompt="What's another state's name?").title()


if answer_state in state:
    writer.penup()
    writer.color('#000fff')
    writer.shapesize(.25, .25)
    writer.goto(coordinates[0])
    writer.write(answer_state, align="left", font=("Arial", 8, "normal"))
else:
    print(False)



turtle.mainloop()