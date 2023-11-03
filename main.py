from turtle import Turtle, Screen

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Kindly predict the race winner", prompt="Which turtle will winn the race? Enter a colour:")
colours = ["red", "orange", "yellow", "blue", "purple", "green"]
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colours[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])

screen.exitonclick()




