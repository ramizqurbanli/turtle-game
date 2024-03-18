import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Game")
screen.bgcolor("black")

# Create the turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("white")
player.penup()
player.speed(0)

# Create food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(random.randint(-290, 290), random.randint(-290, 290))

# Function to move the player
def move_up():
    y = player.ycor()
    y += 20
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= 20
    player.sety(y)

def move_left():
    x = player.xcor()
    x -= 20
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    player.setx(x)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

# Main game loop
while True:
    # Check for collision with food
    if player.distance(food) < 25:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

    screen.update()

# Keep the window open
screen.mainloop()