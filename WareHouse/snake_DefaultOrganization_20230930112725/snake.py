'''
This file contains the SnakeGame class which represents the snake game.
'''
import tkinter as tk
import random
class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="black")
        self.canvas.pack()
        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas)
        self.direction = "Right"
        self.canvas.bind_all("<Key>", self.on_key_press)
        self.update()
    def on_key_press(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"
    def update(self):
        if self.snake.move(self.direction):
            if self.snake.collides_with(self.food):
                self.snake.grow()
                self.food.move()
            self.canvas.after(100, self.update)
        else:
            self.game_over()
    def game_over(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(200, 200, text="Game Over", fill="white", font=("Arial", 20))
class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.body = [(200, 200), (190, 200), (180, 200)]
        self.direction = "Right"
        self.color = "white"
        self.create()
    def create(self):
        for x, y in self.body:
            self.canvas.create_rectangle(x, y, x+10, y+10, fill=self.color)
    def move(self, direction):
        head_x, head_y = self.body[0]
        if direction == "Up":
            new_head = (head_x, head_y-10)
        elif direction == "Down":
            new_head = (head_x, head_y+10)
        elif direction == "Left":
            new_head = (head_x-10, head_y)
        elif direction == "Right":
            new_head = (head_x+10, head_y)
        self.body.insert(0, new_head)
        self.canvas.create_rectangle(new_head[0], new_head[1], new_head[0]+10, new_head[1]+10, fill=self.color)
        self.canvas.delete(self.body[-1][0], self.body[-1][1], self.body[-1][0]+10, self.body[-1][1]+10)
        self.body.pop()
        return self.check_collision()
    def check_collision(self):
        head = self.body[0]
        if head[0] < 0 or head[0] >= 400 or head[1] < 0 or head[1] >= 400:
            return False
        for segment in self.body[1:]:
            if head == segment:
                return False
        return True
    def collides_with(self, food):
        head = self.body[0]
        return head == food.position
    def grow(self):
        tail_x, tail_y = self.body[-1]
        if self.direction == "Up":
            new_tail = (tail_x, tail_y+10)
        elif self.direction == "Down":
            new_tail = (tail_x, tail_y-10)
        elif self.direction == "Left":
            new_tail = (tail_x+10, tail_y)
        elif self.direction == "Right":
            new_tail = (tail_x-10, tail_y)
        self.body.append(new_tail)
        self.canvas.create_rectangle(new_tail[0], new_tail[1], new_tail[0]+10, new_tail[1]+10, fill=self.color)
        if self.collides_with(self.food):
            self.food.move()
class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        self.color = "red"
        self.position = self.generate_position()
        self.create()
    def generate_position(self):
        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        return x, y
    def create(self):
        x, y = self.position
        self.canvas.create_oval(x, y, x+10, y+10, fill=self.color)
    def move(self):
        self.canvas.delete(tk.ALL)
        self.position = self.generate_position()
        self.create()