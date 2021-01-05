import turtle
import pandas as pd


screen = turtle.Screen()
screen.title('U.S. States Game')
screen.setup(725, 491)

image = 'blank_states.gif'
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
answered_states = []
input_prompt_caption = "Let's name some states: "
NUMBER_OF_STATES = 50


while game_on:

    states = list(data['state']) # state
    # coordinates = list(zip(data['x'], data['y']))  # all coordinates
    
    user_answer = screen.textinput(title=f'{score} / {NUMBER_OF_STATES} Guessed States', prompt=input_prompt_caption).title()

    screen.tracer(0) # turn of animation
    if user_answer in states:
        # If the user provided State exist in data['state']
        coordinates = data[data['state'] == user_answer]

        # Provide coordinates if exist
        coors = list(zip(coordinates['x'], coordinates['y']))

        # Write / plot location to screen
        writer = turtle.Turtle('circle')
        writer.penup()
        writer.color('#086a80')
        writer.shapesize(stretch_wid=.20, stretch_len=.20)
        writer.goto(coors[0]) # location to go to
        writer.write(user_answer, align='left', font=('Arial', 12, 'normal'))

        # if the users asnwer wasn't in answered states
        # if not append users asnwer and add 1 to score
        if user_answer not in answered_states:
            answered_states.append(user_answer)
            input_prompt_caption = "What's another state?"
            score += 1
        else: # if user answer in answered states already
            input_prompt_caption = f"{user_answer} was already mentioned."

        # if all states guess prompt succesful caption
        if len(answered_states) == len(states):
            input_prompt_caption = 'Yay! You did it!'

    elif user_answer == 'Quit' or user_answer == 'Answers' or user_answer == 'Print':
        input_prompt_caption = f"You've scored {score} / {NUMBER_OF_STATES}\n US states study sheet created"
        
        # display all missed answers
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.color('#ff0000')

        # logic to displayed and print out missed US states to study
        us_states_study_sheet = []

        for state in states: # i is the state names
            if state not in answered_states: # if i is not in guessed states display them in data
                # print(i)
                # print(data[data['state'] == i])
                coordinates = data[data['state'] == state]
                coors = list(zip(coordinates['x'], coordinates['y']))
                writer.goto(coors[0]) # location to go to
                writer.write(state, align='left', font=('Arial', 12, 'normal'))
                us_states_study_sheet.append(state)
                
        # Print out missed US states to study
        df = pd.DataFrame({'US states to study':us_states_study_sheet})
        df.to_csv('us_states_to_study.csv')
        answered_states = [] # reset correct answers
        score = 0 # reset score

    elif user_answer == 'Exit' or user_answer == 'Bye':
        turtle.bye()
    else:
        input_prompt_caption = 'Oops! Try again please'


    screen.update() # update animation
turtle.mainloop()