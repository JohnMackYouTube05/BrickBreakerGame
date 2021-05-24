from Player import *
import random

class Brick(object):

    numBricks = 0 # How many bricks have been created in the current session.
    brickList = [] # List of all currently drawn bricks.

    def __init__(self, x, y, color:color_rgb=color_rgb(255,0,0)):
        """Creates a new Brick object, with the specified X, Y and Color variables. Not specifying a color will make the brick draw to the screen as red by default."""
        Brick.numBricks += 1 # Counts the brick into the numBricks variable.
        self.__x = x
        self.__y = y
        self.color = color
        self.brick = Rectangle(Point(self.__x, self.__y), Point(self.__x+50,self.__y+10))
        self.doublePoints = False

    def getX(self):
        """Returns the brick's X coordinate."""
        return self.__x

    def getY(self):
        """Returns the brick's Y coordinate."""
        return self.__y

    def destroy(self, win, player=None):
        """Erases the brick from the screen, and removes it from the brick list."""
        self.brick.undraw()
        Brick.brickList.remove(self)

    def draw(self, win):
        """Draws the brick to the screen with the specified color. (Default color is red.)"""
        self.brick.setFill(self.color)
        if self.doublePoints: #If the brick object's double points variable is enabled,
            # it will override the specified color, and re-draw itself as a yellow brick with a 3 pixel thick blue outline.
            self.brick.setWidth(3)
            self.color = color_rgb(255,255,0)
            self.brick.setOutline("blue")
            self.brick.setFill(self.color)
            self.brick.undraw()
        self.brick.draw(win)

    def appendBrick(self):
        """Appends the brick object to the brick list."""
        Brick.brickList.append(self)

def main():
    """Main method for the Brick.py file. Running this Python file on its own will open a Brick Collision Test window, drawing a 6x12 board of bricks, and firing off a ball."""
    win = GraphWin("Brick Collision Test", 600, 600)
    x = 0
    y = 0
    for i in range(6):
        for i in range(12):
            brick = Brick(x, y, color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            brick.draw(win)
            brick.appendBrick()
            #print(Brick.brickList)
            time.sleep(0.025)
            x += 50
        y += 15
        x = 0
    ball = Ball(10, 500, "NW")
    ball.draw(win)
    while not win.closed:
        ball.moveBall(win, ball.getDirection())
        ball.checkCollision(Brick.brickList, win)
        time.sleep(0.05)
        if ball.checkCollision(Brick.brickList, win) == True:
            print("Game Over")
            break
    win.getMouse()
if __name__ == '__main__':
    main()
