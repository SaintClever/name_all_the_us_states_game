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




game_on = True
score = 0

while game_on:
    
    answer_state = screen.textinput(title=f"{score} / 50 Guess the State", prompt="What's another state's name?").title()


    # write to screen
    writer = turtle.Turtle(shape='circle')
    writer.penup()
    writer.shapesize(.25, .25)


    if answer_state in state:
        # If the user provided State exist in data['state']
        state = data[data['state'] == answer_state]

        # Provide coordinates if exist
        coordinates = list(zip(state['x'], state['y']))

        # Plot location
        writer.color('#000fff')
        writer.goto(coordinates[0]) # location to go to
        writer.write(answer_state, align='center', font=('Arial', 10, 'normal'))
        score += 1
    else:
        writer.hideturtle()
        writer.write('Try again please', align='center', font=('Arial', 10, 'normal'))


    # Game status
    if answer_state == 'Off':
        game_on = False



turtle.mainloop()