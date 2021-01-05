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
data = pd.read_csv('states.csv')

game_on = True
score = 0
correct_answers = []
input_prompt_caption = "Let's name some states: "
NUMBER_OF_STATES = 50

while game_on:

    state = list(data['state']) # state
    coordinates = list(zip(data['x'], data['y']))  # coordinates
    user_answer = screen.textinput(title=f'{score} / {NUMBER_OF_STATES} Guessed States', prompt=input_prompt_caption).title()

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
            input_prompt_caption = "What's another state?"
            score += 1

    elif user_answer == 'Quit':
        input_prompt_caption = f"You've scored {score} / {NUMBER_OF_STATES}"
        
        # display all missed answers
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.color('#ff0000')

        # logic to displayed missed states
        for i in state: # i is the state names
            if i not in correct_answers: # if i is not in guessed states display them in data
                # print(i)
                # print(data[data['state'] == i])
                cor = data[data['state'] == i]
                coordinates = list(zip(cor['x'], cor['y']))
                writer.goto(coordinates[0]) # location to go to
                writer.write(i, align='left', font=('Arial', 12, 'normal'))
        correct_answers = [] # reset correct answers
        score = 0 # reset score

    elif len(correct_answers) == len(state):
        input_prompt_caption = 'Yay! You did it!'
    else:
        input_prompt_caption = 'Oops! Try again please'

    screen.update()
turtle.mainloop()