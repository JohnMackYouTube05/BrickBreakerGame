from Player import *
from Brick import *
import time
import random
class Ball(object):


    def __init__(self, x, y, moveX, moveY, direction="N", player=None):
        """Creates a new ball object."""
        self.__x = x #Ball X Coordinate
        self.__y = y #Ball Y Coordinate
        self.__direction = direction #Ball Direction
        self.ball = Circle(Point(self.__x, self.__y), 10) #Circle Object
        self.moveX = moveX #How many pixels the ball is supposed to move on the X axis.
        self.moveY = moveY #How many pixels the ball is supposed to move on the Y axis.
        self.player = player #Links to Player object
        self.alive = True #If ball is alive or not
    def __str__(self):
        """Returns the ball's location (X and Y coordinates), and the curent move speed."""
        return f"Ball Location: ({self.__x}, {self.__y}), Moving {self.__direction}, Move Speed: (X: {self.moveX} Y: {self.moveY})"

    def getX(self):
        """Returns the ball's current X coordinate."""
        return self.__x
    def getY(self):
        """Returns the ball's current Y coordinate."""
        return self.__y
    def getDirection(self):
        """Returns the direction is ball is moving in."""
        return self.__direction
    def checkCollision(self, brickList:list,  win:GraphWin):
        """Checks if the ball is hitting any surface (a brick, or any of the 4 'walls' of the window.)"""
        for brick in brickList: #Iterate through every brick in the list
            if Circle.testCollision_CircleVsRectangle(self.ball, brick.brick): #Test collision between ball and current brick
                dirList = ["NW", "NE", "SW", "SE"] #Direction list
                self.moveX = random.randint(1, 10)
                self.moveY = random.randint(1, 10)
                brick.destroy(win, self.player) #Destroy brick
                if brick.doublePoints: #If brick is double points and ball hits it, set player's double points attribute to True.
                    self.player.doublePoints = True #Set 2x points to True
                if self.player is not None: #Player would equal none in the testing environment.
                    if self.player.doublePoints: #If 2x Points is enabled
                        self.player.setScore(win, self.player.getScore() + 200) #Increase score by 200 points
                    else: #If 2x points isn't enabled
                        self.player.setScore(win, self.player.getScore() + 100) #Increase score by 100 points
                self.moveBall(win, self.moveX, self.moveY, dirList[random.randint(0, 3)]) #Move ball in random direction
                #return True
        if self.getX() < 0 and self.getDirection() != "SW": #If ball hits left wall, and is coming from the lower right
            self.moveX = random.randint(1, 10)
            self.moveY = random.randint(1, 10)
            self.moveBall(win, self.moveX, self.moveY, "NE") #Move ball up and to the right
        elif self.getX() < 0 and self.getDirection() == "SW": #If ball hits left wall, and is coming from the lower left
            self.moveX = random.randint(1, 10)
            self.moveY = random.randint(1, 10)
            self.moveBall(win, self.moveX, self.moveY, "SE") #Move ball down and to the right

        elif self.getY() <= 0 and self.getDirection() != "NW": #If ball hits top wall, and is coming from the upper right
            self.moveX = random.randint(1, 10)
            self.moveY = random.randint(1, 10)
            self.moveBall(win, self.moveX, self.moveY, "SE") #Move ball down and to the right
           # return True
        elif self.getY() <= 0 and self.getDirection() == "NW": #If ball hits top wall and is coming from the upper left
            self.moveX = random.randint(1, 10)
            self.moveY = random.randint(1, 10)
            self.moveBall(win, self.moveX, self.moveY, "SW") #Move ball down and to the left
            #return True
        elif self.getX() > win.getWidth(): #If ball hits right wall
            self.moveX = random.randint(1, 10)
            self.moveY = random.randint(1, 10)
            self.moveBall(win, self.moveX, self.moveY, "NW") #Move ball up and to the left
            #return True
        elif self.getY() > win.getHeight(): #If ball hits bottom wall, destroy ball
            return True

        if self.player != None: #If ball hits player (providing there is one, which would only be false in a testing environment.)
            if Circle.testCollision_CircleVsRectangle(self.ball, self.player.player): #Test collision between the ball and the player.
                self.moveX = random.randint(1, 10)
                self.moveY = random.randint(1, 10)
                if self.getDirection() == "SW": #If ball comes from upper left
                    self.moveBall(win, self.moveX, self.moveY, "NW") #Move ball up and to the right
                elif self.getDirection() == "SE": #If ball comes from upper right
                    self.moveBall(win, self.moveX, self.moveY, "NE") #Move ball up and to the left
        return False

    def draw(self, win:GraphWin):
        """Draws the ball to the screen."""
        self.ball.setFill("white") #Make the ball white
        self.ball.draw(win) #Draw ball
        self.alive = False
    def destroy(self):
        """Erases the ball from the screen, and removes it from the balls list."""
        self.ball.undraw() #Undraws the ball
        self.player.balls.remove(self) #Removes ball from ball list
    def moveBall(self, win:GraphWin,  x, y, direction = "NW"):
        """Moves the ball a specified amount of pixels in the specified direction. Valid directions are NW, NE, SE, and SW. Pass them to this method as a string."""
        if direction == 'NW':
            self.__direction = direction #Set direction
            self.__x -= x #Subtract specified value from X
            self.__y -= y #Subtract specified value from Y
            self.ball.move(x*-1, y*-1) #Move ball up and to the left
        elif direction == "NE":
            self.__direction = direction
            self.__x += x #Add specified value to X
            self.__y -= y #Subtract specified value from Y
            self.ball.move(x, y*-1) #Move ball up and to the right
        elif direction == "SW":
            self.__direction = direction #Set direction
            self.__x -= x #Subtract specified value from X
            self.__y += y #Add specified value to Y
            self.ball.move(x*-1, y) #Move ball down and to the left
        elif direction == "SE":
            self.__direction = direction #Set direction
            self.__x += x #Add specified value to X
            self.__y += y #Add specified value to Y
            self.ball.move(x, y) #Move ball down and to the right


def main():
    """Main method for this class. Running this specific python file will result in a ball test window appearing."""
    win = GraphWin("Ball Test", 600, 600) #Create and open new window
    ball = Ball(10, 500, random.randint(1, 10), random.randint(1, 10), "NW") #Create new ball
    ball.draw(win) #Draw ball
    while not win.closed: #While window is open
        ball.moveBall(win, ball.moveX, ball.moveY, ball.getDirection()) #Move ball
        ball.checkCollision(Brick.brickList, win) #Check collision against the 4 walls
        time.sleep(0.05) #Sleep for .05 seconds so the ball doesn't move at MACH-5 speeds.
    win.getMouse() #Wait for user to click mouse again, and then close the window.

if __name__ == '__main__':
    main() #Run ball test
