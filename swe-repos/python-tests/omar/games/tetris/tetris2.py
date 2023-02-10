import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Tetris")
screen.bgcolor("black")

# Define the blocks
block_colors = ["red", "yellow", "blue", "green", "purple", "orange", "cyan"]
block_shapes = [    [(0, 0), (1, 0), (0, 1), (1, 1)],  # Square
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # Long block
    [(0, 0), (1, 0), (2, 0), (2, 1)],  # L-shape
    [(0, 0), (1, 0), (2, 0), (1, 1)],  # T-shape
    [(0, 0), (1, 0), (2, 0), (2, -1)],  # Reverse L-shape
    [(0, 0), (0, 1), (0, 2), (1, 2)],  # Reverse T-shape
    [(0, 0), (1, 0), (1, 1), (2, 1)],  # Z-shape
]

# Create the blocks
blocks = []
for shape in block_shapes:
    block = turtle.Turtle()
    block.speed(0)
    block.shape("square")
    block.color(random.choice(block_colors))
    block.penup()
    block.goto(0, 0)
    blocks.append(block)

# Game loop
while True:
    for block in blocks:
        block.forward(10)

        # Check for collision with the wall
        if block.xcor() > 200:
            block.right(180)

        # Check for collision with the floor
        if block.ycor() < -200:
            block.sety(-200)



# Start the screen
    screen.mainloop()
