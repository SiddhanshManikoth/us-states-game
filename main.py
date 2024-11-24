import turtle
import pandas

image = "blank_states_img.gif"
turtle.Screen().addshape(image)
turtle.shape(image)
turtle.Screen()
turtle.title("U.S states games")
writing_turtle = turtle.Turtle()
writing_turtle.hideturtle()
writing_turtle.penup()
country_data = pandas.read_csv("50_states.csv")
country_state_names = list(country_data.state)

score = 0
game_is_on = True
while game_is_on:
    user_answer = turtle.Screen().textinput(title="guess the state", prompt="what's the another state name?")
    for state in country_state_names:
        if user_answer.title() == state:
            state_coordinates = country_data[country_data.state == state]
            x = int(state_coordinates.x.iloc[0])
            y = int(state_coordinates.y.iloc[0])
            writing_turtle.goto(x, y)
            writing_turtle.write(state, align="center", font=('Arial', 8, 'normal'))
            country_state_names.remove(state)
            score += 1
        if len(country_state_names) == 0:
            print("you win!!")
            game_is_on = False
        if user_answer == "exit":
            game_is_on = False

missed_country = pandas.DataFrame(country_state_names)
missed_country.to_csv("states_to_learn.csv")
