from MultiballBrick import *

def main():
    """Main method for the Brick Breaker game itself. This is the Python file to run in order to play the game."""
    ######################
    #  INITIALIZE GAME   #
    ######################
    win = GraphWin( "Brick Breaker Game - by John Mack", 600, 600) # Open a new 600x600 square window
    win.setWindowIcon("GameIcon.png")
    plr = Player(0, 500) # Create player object
    x = 0 # Sets temporary x variable
    y = 20 # Sets temporary y variable
    background = Image(Point(300,300), "Rainbow-Pixels-1-Opacity-60.png")

    background.draw(win)
    for i in range(6): # Draw 6x12 board of bricks, which are filled with random RGB colors.
        for i in range(12):
            brick = Brick(x, y, color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            brick.draw(win)
            brick.appendBrick()
            #print(Brick.brickList)
            time.sleep(0.025)
            x += 50
        y += 15
        x = 0
    plr.draw(win) # Draw player to the screen
    plr.score.draw(win) # Draw score display
    powerUpBrick = random.randint(0, len(brick.brickList)-1) # Choose which brick will be the 2x Points brick.
    brick.brickList[powerUpBrick].doublePoints = True # Set that brick's doublePoints attribute to True.
    brick.brickList[powerUpBrick].draw(win) # Redraw that brick
    ballsLeftTxt = Text(Point(500, 10), f"Balls Left: {plr.ballsLeft}") # Initialize the ball counter display
    ballsLeftTxt.draw(win) # Draw the ball counter display
    multiballBrick = random.randint(0, len(brick.brickList)-1) # Choose which brick will be the multiball brick.
    oldBrickX = brick.brickList[multiballBrick].getX() # Get the old brick's X coordinate and store it.
    oldBrickY = brick.brickList[multiballBrick].getY() # Get the old brick's X coordinate and store it.
    brick.brickList[multiballBrick].brick.undraw() # Undraw the old brick.
    brick.brickList.pop(multiballBrick) #Remove the old brick from the list
    brick.brickList.insert(multiballBrick, MultiBallBrick(oldBrickX, oldBrickY, player=plr)) # Insert a new multi-ball brick variation into the list, in the place index of the old one.
    brick.brickList[multiballBrick].draw(win) # Draw the new multi-ball brick
    ##################
    # END INITIALIZE #
    ##################

    # Actual Game code starts here
    while plr.ballsLeft > 0:  # While the player has at least 1 ball left for them
        direction = getDirection(win, plr.getDirection()) # Get direction
        mouse = win.checkMouse()  # Check when player clicks their mouse
        plr.move(direction)  # Move player based on key-presses.
        time.sleep(.02)  # Sleep for .02 seconds so the player doesn't fly off the screen at MACH-5 Speeds

        if mouse != None: # Player clicked their mouse
            randX = random.randint(1, 10)
            randY = random.randint(1, 10)
            if mouse.getX() >= plr.getX(): # If mouse pointer clicked to the right of the player
                plr.fireBall(win, randX, randY, "NE") # Fire ball heading up and to the right
                plr.ballsLeft -= 1 # Decrease ballsLeft by 1.
                for b in plr.balls:
                    b.moveX = randX
                    b.moveY = randY
                #mouse = None
                ballsLeftTxt.setText(f"Balls Left: {plr.ballsLeft}") # Update ball counter.
                while len(plr.balls) != 0: # While any balls are still on screen
                    for b in plr.balls: # Iterate through every ball in the list
                        
                        # b.moveX = randX
                        # b.moveY = randY
                        b.moveBall(win, b.moveX, b.moveY, b.getDirection()) # Move ball
                        b.checkCollision(Brick.brickList, win) # Check if ball is hitting bricks or the player or any walls.
                        if b.getY() >= win.getHeight(): # If ball is hitting bottom wall
                            b.destroy() # Remove ball from the list

                    direction = getDirection(win, plr.getDirection()) # Get direction based on key-presses.
                    plr.move(direction) # Move player accordingly
                    time.sleep(0.05) # Sleep for .05 seconds so the game doesn't perform at the speed of light.
                    if len(Brick.brickList) == 0:
                        break
            else: # If mouse pointer clicked to the left of the player.
                plr.fireBall(win, randX, randY, "NW") # Fire ball heading up and to the left.
                plr.ballsLeft -= 1 # Decrease ball counter
                ballsLeftTxt.setText(f"Balls Left: {plr.ballsLeft}") # Update ball counter
                for b in plr.balls:
                    b.moveX = randX
                    b.moveY = randY
               # mouse = None

                while len(plr.balls) != 0: # While any balls are still on screen
                    for b in plr.balls: # Iterate through every ball in the list.
                        
                        b.moveBall(win, b.moveX, b.moveY, b.getDirection()) # Move ball
                        b.checkCollision(Brick.brickList, win) # Check if ball is hitting bricks or the player or any walls.
                        if b.getY() >= win.getHeight(): # If ball is hitting bottom wall
                            b.destroy() # Remove ball from the list

                    direction = getDirection(win, plr.getDirection()) # Check direction based on key-presses.
                    plr.move(direction) # Move player accordingly.
                    time.sleep(0.05) # Sleep for .05 seconds so the game doesn't perform at the speed of light.
                    if len(Brick.brickList) == 0:
                        break

    if len(Brick.brickList) != 0:
        print(f"Game Over! Your final score is {plr.getScore()} points!") # Once game is over, print the player's score to the console (if it's even visible)
        #Draw "Game Over" pop-up
        #Background
        gameOverFrame = Rectangle(Point(0, 200), Point(600, 400))
        gameOverFrame.setFill("red")
        gameOverFrame.draw(win)
        #Title
        gameOverTitle = Text(Point(win.getWidth()/2, 250), "Game Over!")
        gameOverTitle.setTextColor("white")
        gameOverTitle.setSize(24)
        gameOverTitle.setStyle("bold")
        gameOverTitle.draw(win)
        #Message displaying the player's final score
        gameOverSubtitle = Text(Point(win.getWidth()/2, 350), f"")
        gameOverTxt = f"""
Your final score is {plr.getScore()} points!
Press anywhere inside the window to close it.
"""
        gameOverSubtitle.setText(gameOverTxt)
        gameOverSubtitle.setTextColor("white")
        gameOverSubtitle.setSize(16)
        gameOverSubtitle.draw(win)
        win.getMouse() # Wait for player to click their mouse again, and then close the window.
        # Game Finished
    else:
        print(f"Congratulations! You broke all of the bricks! Your final score is {plr.getScore()} points!")
        #Draw "You Win" pop-up
            #Background
        youWinFrame = Rectangle(Point(0, 200), Point(600, 400))
        youWinFrame.setFill(color_rgb(0, 255, 0))
        youWinFrame.draw(win)
        #Title
        youWinTitle = Text(Point(win.getWidth()/2, 250), "YOU WIN!")
        youWinTitle.setTextColor("black")
        youWinTitle.setSize(24)
        youWinTitle.setStyle("bold")
        youWinTitle.draw(win)
        #Message displaying the player's final score
        youWinSubtitle = Text(Point(win.getWidth()/2, 350), f"")
        youWinTxt = f"""
Congratulations, you broke all of the bricks!
Your final score is {plr.getScore()} points!
Press anywhere inside the window to close it.
"""
        youWinSubtitle.setText(youWinTxt)
        youWinSubtitle.setTextColor("black")
        youWinSubtitle.setSize(16)
        youWinSubtitle.draw(win)
        win.getMouse()

if __name__ == '__main__':
    main() #Run the game
