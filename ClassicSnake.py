import random
from turtle import Turtle, Screen
from time import sleep as delay

# Constants for game dimensions and settings
WIDTH, HEIGHT = 500, 500
GRID_SIZE = 20
START_LENGTH = 3
DELAY = 0.3


class Snake:
    def __init__(self):
        self.window = self.setup_screen()
        self.draw_grid()
        self.snake = self.create_snake()
        self.set_colors()
        self.foods = []
        self.flag = 0
        self.score = 0
        self.scoreboard = self.create_scoreboard()
        self.setup_controls()

    def setup_screen(self):
        """
        Set up the game screen.
        :return: Screen object
        """
        screen = Screen()
        screen.bgcolor('black')
        screen.setup(width=WIDTH + 200, height=HEIGHT + 200)
        screen.tracer(0)  # Turn off automatic screen updates
        return screen

    def draw_grid(self):
        """
        Draw the grid on the screen.
        """
        grid_turtle = Turtle()
        grid_turtle.hideturtle()
        grid_turtle.color((0.075, 0.075, 0.075))
        grid_turtle.speed(0)

        for x in range(-WIDTH // 2, WIDTH // 2, GRID_SIZE):
            grid_turtle.penup()
            grid_turtle.goto(x, -HEIGHT // 2)
            grid_turtle.pendown()
            grid_turtle.goto(x, HEIGHT // 2)

        for y in range(-HEIGHT // 2, HEIGHT // 2, GRID_SIZE):
            grid_turtle.penup()
            grid_turtle.goto(-WIDTH // 2, y)
            grid_turtle.pendown()
            grid_turtle.goto(WIDTH // 2, y)

    def create_snake(self):
        """
        Create the initial snake.
        :return: List of Turtle objects representing the snake
        """
        snake = []
        for i in range(START_LENGTH):
            snake_part = Turtle()
            snake_part.speed(0)
            snake_part.shape('square')
            snake_part.color('black')
            snake_part.penup()
            snake_part.goto(-200 + i * GRID_SIZE, 0)
            snake.append(snake_part)
        return snake[::-1]  # Reverse to make the head the last part created

    def set_colors(self):
        """
        Set colors for each part of the snake.
        """
        for i, part in enumerate(self.snake):
            part.color(0, (len(self.snake) - i) / len(self.snake), 0)

    def setup_controls(self):
        """
        Set up keyboard controls for the snake.
        """
        self.window.listen()
        self.window.onkey(lambda: self.turn_left(), 'Left')
        self.window.onkey(lambda: self.turn_right(), 'Right')
        self.window.onkey(lambda: self.turn_up(), 'Up')
        self.window.onkey(lambda: self.turn_down(), 'Down')

    def create_scoreboard(self):
        """
        Create the scoreboard to display the score.
        :return: Turtle object for the scoreboard
        """
        scoreboard = Turtle()
        scoreboard.speed(0)
        scoreboard.color('white')
        scoreboard.penup()
        scoreboard.hideturtle()
        scoreboard.goto(WIDTH // 2 - 100, HEIGHT // 2 - 40)
        scoreboard.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))
        return scoreboard

    def update_scoreboard(self):
        """
        Update the scoreboard with the current score.
        """
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def add_food(self):
        """
        Add a food item to the screen.
        """
        food = Turtle()
        food.speed(0)
        food.shape('square')
        food.color((0.35, 0.35, 0.35))
        food.penup()
        x = random.randint(-WIDTH // 2 // GRID_SIZE + 1, WIDTH // 2 // GRID_SIZE - 1) * GRID_SIZE
        y = random.randint(-HEIGHT // 2 // GRID_SIZE + 1, HEIGHT // 2 // GRID_SIZE - 1) * GRID_SIZE
        food.goto(x, y)
        self.foods.append(food)

    def move_snake(self):
        """
        Move the snake forward and check for collisions.
        :return: Boolean indicating if the snake is still alive
        """
        head = self.snake[0]
        previous_positions = [part.position() for part in self.snake]

        # Move the body
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(*previous_positions[i - 1])

        # Move the head
        head.forward(GRID_SIZE)

        # Check for collisions with walls
        if abs(head.xcor()) > WIDTH // 2 or abs(head.ycor()) > HEIGHT // 2:
            return False

        # Check for collisions with the body
        for part in self.snake[1:]:
            if head.distance(part) < GRID_SIZE:
                return False

        return True

    def turn_left(self):
        """
        Turn the snake left.
        """
        head = self.snake[0]
        if head.heading() != 0:
            head.setheading(180)

    def turn_right(self):
        """
        Turn the snake right.
        """
        head = self.snake[0]
        if head.heading() != 180:
            head.setheading(0)

    def turn_up(self):
        """
        Turn the snake up.
        """
        head = self.snake[0]
        if head.heading() != 270:
            head.setheading(90)

    def turn_down(self):
        """
        Turn the snake down.
        """
        head = self.snake[0]
        if head.heading() != 90:
            head.setheading(270)

    def check_food_collision(self):
        """
        Check if the snake's head collides with any food items.
        """
        head = self.snake[0]
        for food in self.foods:
            if head.distance(food) < GRID_SIZE:
                self.add_body()
                food.hideturtle()
                self.foods.remove(food)
                self.score += 1
                self.update_scoreboard()

    def add_body(self):
        """
        Add a new segment to the snake.
        """
        tail = self.snake[-1]
        new_part = Turtle()
        new_part.speed(0)
        new_part.shape('square')
        new_part.color('black')
        new_part.penup()
        new_part.goto(*tail.position())
        self.snake.append(new_part)
        self.set_colors()  # Update colors to reflect the new length

    def run(self):
        """
        Run the main game loop.
        """
        while True:
            self.window.update()  # Update the screen

            if not self.move_snake():  # Move the snake and check for game over
                break  # End the game if snake collides

            self.check_food_collision()  # Check if snake eats food

            if self.flag == 0 or (self.flag % 5 == 0 and len(self.foods) < 10):
                self.add_food()  # Add food periodically

            self.flag += 1
            delay(DELAY)  # Control the speed of the game


if __name__ == '__main__':
    snake_game = Snake()
    snake_game.run()
