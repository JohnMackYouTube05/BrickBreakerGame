from Brick import *
from Player import *

class MultiBallBrick(Brick):

    def __init__(self, x, y, player, color:color_rgb=color_rgb(255,0,0)):
        """Creates a new multi-ball brick, which is a variation of the 'Brick' class."""
        super().__init__(x, y, color)
        self.__x = x
        self.__y = y
        self.color = color
        self.player = player
        self.balls = []

    def destroy(self, win, player:Player):
        """The method that sets this brick apart from a normal brick. Upon destroying this brick with your ball, 5 new balls will spawn where the player is currently at, and all of them will start moving in random directions."""
        self.brick.undraw()
        Brick.brickList.remove(self)
        dirList = ["NW", "NE", "SW", "SE"]
        plr = self.player
        for i in range(5):
            randX = random.randint(1, 10)
            randY = random.randint(1, 10)
            direction = dirList[random.randint(0, 3)]
            player.fireBall(win, randX, randY, direction)
            #self.balls.append(ball)
        # while len(self.balls) != 0:
        #     for b in self.balls:
        #         b.moveBall(direction)
        #         b.checkCollision(Brick.brickList, win)
        #         plr.ball.moveBall(win, plr.ball.getDirection())
        #         plr.ball.checkCollision(Brick.brickList, win)
        #         direction = getDirection(win, plr.getDirection())
        #         plr.move(direction)
        #         if plr.ball.getY() > win.getHeight():
        #             b.ball.undraw()
        #             self.balls.remove(b)
        #         time.sleep(0.05)

def getDirection(win:GraphWin, direction):
    """Gets direction of the player based on key-presses."""
    key = win.checkKey().lower()
    if key == 'a':
        return "W"
    elif key == 'd':
        return "E"
    else:
        return ""

