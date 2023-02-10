import turtle
import random
import tkinter as TK

# Set up the screen
screen = turtle.Screen()
screen.title("2D Tetris")
screen.bgcolor("black")

# Define the shapes for each of the tetrominos
tetrominos = [
    [[1, 1, 1, 1]],

    [[2, 2, 2],
     [0, 2, 0]],

    [[0, 3, 3],
     [3, 3, 0]],

    [[4, 4, 0],
     [0, 4, 4]],

    [[0, 5, 0],
     [5, 5, 5]],

    [[6, 6, 6, 6]],

    [[7, 7],
     [7, 7]]
]

colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "purple",
    "orange",
    "cyan"
]

# Define the shape class
class Shape:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.row = 0
        self.col = 5

    def draw(self, pen):
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                if self.shape[row][col] != 0:
                    pen.color(colors[self.color])
                    pen.goto(col + self.col, row + self.row)
                    pen.stamp()

    def move_left(self):
        self.col -= 1

    def move_right(self):
        self.col += 1

    def move_down(self):
        self.row -= 1

# Define the game class
class Game:
    def __init__(self):
        self.grid = [[0 for x in range(10)] for y in range(20)]
        self.shape = Shape(random.choice(tetrominos),
                           random.randint(0, len(colors) - 1))
        self.running = True

    def run(self):
        while self.running:
            self.shape.move_down()
            screen.ontimer(self.run, 500)

# Start the game
game = Game()
game.run()

screen.exitonclick()
