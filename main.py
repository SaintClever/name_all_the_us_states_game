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


game_on = True
score = 0
correct_answers = []


while game_on:

    # state
    state = list(data['state'])

    # coordinates
    coordinates = list(zip(data['x'], data['y']))


    user_answer = screen.textinput(title=f"{score} / 50 Guess the State", prompt="What's another state's name?").title()


    # write to screen
    writer = turtle.Turtle()
    writer.penup()
    writer.shape('circle')



    if user_answer in state:
        # If the user provided State exist in data['state']
        state = data[data['state'] == user_answer]

        # Provide coordinates if exist
        coordinates = list(zip(state['x'], state['y']))

        # Plot location
        writer.clear() # clear previous text
        writer.color('#086a80')
        writer.shapesize(stretch_wid=.20, stretch_len=.20)
        writer.goto(coordinates[0]) # location to go to
        writer.write(user_answer, align='left', font=('Arial', 12, 'normal'))

        # Check to see if the users asnwer was or wan't in correct answers
        # if not append and add 1 to score else do nothing
        if user_answer not in correct_answers:
            correct_answers.append(user_answer)
            score += 1
            
    # elif user_answer == 'Reset':
    #     screen.clear()
    #     correct_answers = []
    #     score = 0

    # elif user_answer == 'Off': # Game status
    #     game_on = False

    # elif len(correct_answers) == len(state):
    #     writer.clear() # clear previous text
    #     writer.home() # return home
    #     writer.write('You did it!', align='center', font=('Arial', 12, 'normal'))

        
    else:
        writer.clear() # clear previous text
        writer.write('Try again please', align='center', font=('Arial', 12, 'normal'))

    
turtle.mainloop()