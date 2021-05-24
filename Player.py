from graphics import *
import time
from Ball import *
class Player(object):
    def __init__(self, x, y, color=color_rgb(0,0,170), currentDirection="N"):
        """Creates a new player object. You only need 1 of these."""
        self.__x = x
        self.__y = y
        self.color = color
        self.alive = True
        self.ballsLeft = 3
        self.score = Text(Point(300, 10), "Score: 0")
        self.__direction = currentDirection
        self.player = Rectangle(Point(self.__x, self.__y), Point(self.__x+120, self.__y+25))
        self.doublePoints = False
        self.balls = []
    def __str__(self):
        """Returns the location of the player in format (X, Y)"""
        return f"Player Location: ({self.__x}, {self.__y})"
    def getDirection(self):
        """Returns the direction the player is moving in currently."""
        return self.__direction

    def getX(self):
        """Returns the player's X coordinate."""
        return self.__x

    def getY(self):
        """Returns the player's Y coordinate."""
        return self.__y

    def checkBalls(self):
        """Returns how many balls are left for the player."""
        return self.ballsLeft

    def draw(self, win:GraphWin):
        """Draws the player object to the window."""
        self.player.setFill(self.color)
        self.player.draw(win)
    def fireBall(self, win:GraphWin, x, y, direction="NW"):
        """Instantiates and creates a new ball, and adds it to the ball list."""
        self.ball = Ball(self.__x+40, self.__y-20, x, y, direction, player=self)
        self.ball.draw(win)
        self.ball.moveBall(win, x, y, direction)
        self.balls.append(self.ball)


    def move(self, direction):
        """Moves the player left or right. Valid directions are W and E."""
        self.__direction = direction
        if direction == "W":
            self.__x = self.__x - 10
            self.player.move(-10, 0)
        elif direction == "E":
            self.__x = self.__x + 10
            self.player.move(10, 0)
    def getScore(self):
        """Returns the current score of the player as an integer."""
        score = int(self.score.getText().split(": ")[1])
        return score
    def setScore(self, win:GraphWin, newScore):
        """Sets the player's score variable to the specified number."""
        self.score.undraw()
        self.score.setText(f"Score: {newScore}")
        self.score.draw(win)
def getDirection(win:GraphWin, direction):
    """Return the player's direction based on key-presses."""
    key = win.checkKey().lower()
    if key == 'a':
        return "W"
    elif key == 'd':
        return "E"
    else:
         return ""
def main():
    """Main method of the player. Running this Python file on its own will open a Player Test window, verifying that the player can move."""
    win = GraphWin("Player Test", 600,600)
    player = Player(0, 500)
    player.draw(win)
    win.getMouse()
    player.fireBall(win)
    while not win.closed:
        direction = getDirection(win, player.getDirection())
        player.move(direction)

        time.sleep(.02)
    win.getMouse()

if __name__ == '__main__':
    main()


