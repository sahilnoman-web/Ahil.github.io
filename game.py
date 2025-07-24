import tkinter as tk
import random

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
PLAYER_SPEED = 10
BULLET_SPEED = 15
OBSTACLE_SPEED = 5
SNOWFLAKE_COUNT = 50

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Snowy Mario-Style Game")
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="skyblue")
        self.canvas.pack()

        self.snowflakes = [self.canvas.create_oval(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT),
                                                   random.randint(3, 6), random.randint(3, 6),
                                                   fill="white", outline="white") for _ in range(SNOWFLAKE_COUNT)]

        self.score = 0
        self.score_text = self.canvas.create_text(700, 30, text="Score: 0", font=("Arial", 16), fill="white")

        self.player = self.canvas.create_rectangle(100, 400, 140, 440, fill="red")
        self.bullets = []
        self.obstacles = []
        self.running = True

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.shoot)

        self.game_loop()

    def move_left(self, event):
        self.canvas.move(self.player, -PLAYER_SPEED, 0)

    def move_right(self, event):
        self.canvas.move(self.player, PLAYER_SPEED, 0)

    def shoot(self, event):
        px1, py1, px2, py2 = self.canvas.coords(self.player)
        bullet = self.canvas.create_oval(px2, py1 + 10, px2 + 10, py1 + 20, fill="yellow")
        self.bullets.append(bullet)

    def create_obstacle(self):
        top = random.randint(350, 400)
        obs = self.canvas.create_rectangle(WINDOW_WIDTH, top, WINDOW_WIDTH + 30, top + 40, fill="green")
        self.obstacles.append(obs)

    def update_snow(self):
        for snowflake in self.snowflakes:
            self.canvas.move(snowflake, 0, random.randint(1, 3))
            if self.canvas.coords(snowflake)[1] > WINDOW_HEIGHT:
                self.canvas.coords(snowflake, random.randint(0, WINDOW_WIDTH), 0)

    def game_loop(self):
        if not self.running:
            return

        self.update_snow()

        for bullet in self.bullets[:]:
            self.canvas.move(bullet, BULLET_SPEED, 0)
            if self.canvas.coords(bullet)[0] > WINDOW_WIDTH:
                self.canvas.delete(bullet)
                self.bullets.remove(bullet)

        if random.randint(1, 25) == 1:
            self.create_obstacle()

        for obs in self.obstacles[:]:
            self.canvas.move(obs, -OBSTACLE_SPEED, 0)
            if self.canvas.coords(obs)[2] < 0:
                self.canvas.delete(obs)
                self.obstacles.remove(obs)

            if self.check_collision(self.player, obs):
                self.game_over()

            for bullet in self.bullets:
                if self.check_collision(bullet, obs):
                    self.canvas.delete(obs)
                    self.canvas.delete(bullet)
                    self.obstacles.remove(obs)
                    self.bullets.remove(bullet)
                    self.score += 1
                    self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
                    break

        self.root.after(50, self.game_loop)

    def check_collision(self, item1, item2):
        x1, y1, x2, y2 = self.canvas.coords(item1)
        a1, b1, a2, b2 = self.canvas.coords(item2)
        return not (x2 < a1 or x1 > a2 or y2 < b1 or y1 > b2)

    def game_over(self):
        self.running = False
        self.canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 30,
                                text="GAME OVER", font=("Arial", 30), fill="red")
        retry_btn = tk.Button(self.root, text="Retry", font=("Arial", 14), command=self.retry)
        self.canvas.create_window(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 10, window=retry_btn)

    def retry(self):
        self.canvas.delete("all")
        self.__init__(self.root)

root = tk.Tk()
game = Game(root)
root.mainloop()
