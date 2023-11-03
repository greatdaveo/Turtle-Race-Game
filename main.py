from turtle import Turtle, Screen
import  random

is_race_on = False
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Kindly predict the race winner", prompt="Which turtle will winn the race? Enter a colour:")
colours = ["red", "orange", "yellow", "blue", "purple", "green"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    each_turtle = Turtle(shape="turtle")
    each_turtle.color(colours[turtle_index])
    each_turtle.penup()
    each_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(each_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Your prediction was correct! The {winning_color} won the race!")
            else:
                print(f"Your prediction was wrong! The {winning_color} won the race!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()




