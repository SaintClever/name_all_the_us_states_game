import turtle
import pandas as pd


screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


# Capture mouse clicks
# def capture_mouse_clicks_cor(x, y):
#     print(x, y)
# turtle.onscreenclick(capture_mouse_clicks_cor)


# data
data = pd.read_csv('50_states.csv')

game_on = True
score = 0
correct_answers = []
INPUT_PROMPT_CAPTION = "What's another state's name?"


while game_on:

    state = list(data['state']) # state
    coordinates = list(zip(data['x'], data['y']))  # coordinates
    user_answer = screen.textinput(title=f'{score} / 50 Guessed States', prompt=INPUT_PROMPT_CAPTION).title()

    screen.tracer(0)
    if user_answer in state:
        # If the user provided State exist in data['state']
        state = data[data['state'] == user_answer]

        # Provide coordinates if exist
        coordinates = list(zip(state['x'], state['y']))

        # Write / plot location to screen
        writer = turtle.Turtle('circle')
        writer.penup()
        writer.color('#086a80')
        writer.shapesize(stretch_wid=.20, stretch_len=.20)
        writer.goto(coordinates[0]) # location to go to
        writer.write(user_answer, align='left', font=('Arial', 12, 'normal'))

        # Check to see if the users asnwer was or wan't in correct answers
        # if not append and add 1 to score else do nothing
        if user_answer not in correct_answers:
            correct_answers.append(user_answer)
            INPUT_PROMPT_CAPTION = "What's another state's name?"
            score += 1

    elif user_answer == 'Quit':
        INPUT_PROMPT_CAPTION = "You've scored {score} / 50"
        correct_answers = []
        score = 0

    elif len(correct_answers) == len(state):
        INPUT_PROMPT_CAPTION = 'Yay! You did it!'
    else:
        INPUT_PROMPT_CAPTION = 'Oops! Try again please'

    screen.update()
turtle.mainloop()