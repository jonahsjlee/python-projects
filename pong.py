# Pong (Starter Code)

import uvage
camera = uvage.Camera(800,600)

p_width = 10
p_height = 80
ball_velocity = 15
player_speed = 14
p1_score = 0
p2_score = 0
game_on = False

ticker = 0

walls = [
    uvage.from_color(400, 600, "green", 1000, 20),
    uvage.from_color(400, 0, "green", 1000, 20),
]

p1 = uvage.from_color(20, 400, "red", 15, 100)
p2 = uvage.from_color(780, 400, "yellow", 15, 100)
ball = uvage.from_color(400,300, "green", 20, 20)

ball.xspeed = ball_velocity
ball.yspeed = ball_velocity

def tick():

    global game_on
    global p1_score
    global p2_score

    # --- BALL MOVEMENT ---
    # We use the game_on boolean variable to determine
    # if we should be moving the ball or not at this time
    # because we want it to stay still before the game
    # starts.  Add code to move the ball according to
    # the ball speed if game_on is True.
    # i.e. if game_on:
    #         your code here to move ball

    # ------- INPUT ---------
    if uvage.is_pressing("up arrow"):
        game_on = True
    # We want the game to start when the space bar
    # is pressed.  Add the rest of the code here to
    # control paddle movement.  We suggest W and S
    # for the red (left) player and Up and Down for
    # the yellow (right) player.  Note that there
    # is a player_speed variable you can use.

    # ----- COLLISION DETECTION -----
    # First, handle collisions between all of the
    # walls and the ball.  If the ball touches any
    # wall, reverse the yspeed of the ball.
    # Next, handle collisions between the paddles
    # and the ball.  If the ball touches either paddle,
    # reverse its xspeed.
    # These are very simplistic rules for bounces.
    # Basically, every bounce will be 45 degrees. If
    # you want to do more, go ahead, but it's not
    # required
    # ----- SCORING ------
    # When the ball's x coordinate goes off the screen,
    # you need to add 1 to the appropriate player's
    # score, move the ball back to the middle of the
    # screen, and set game_on to False.  You will
    # probably have two if statements here - one for
    # if the ball goes off on the left and one if
    # it goes off on the right.


    # ----- DRAW METHODS --------
    # We have provided all of the draw methods for you.
    # You do not need to add anything here.
    camera.clear("black")
    camera.draw(uvage.from_text(300, 50, str(p1_score), 50, "Red", bold=True))
    camera.draw(uvage.from_text(500, 50, str(p2_score), 50, "Yellow", bold=True))

    # Draw all the walls
    for wall in walls:
        camera.draw(wall)

    # Draw the player paddles and the ball
    camera.draw(p1)
    camera.draw(p2)
    camera.draw(ball)

    # ---- CHECKING FOR WIN ----
    if p1_score >= 10:
        camera.draw(uvage.from_text(400, 100, "Red Wins!", 40, "Red", bold=False))
        uvage.pause()
    if p2_score >= 10:
        camera.draw(uvage.from_text(400, 100, "Yellow Wins!", 40, "Yellow", bold=False))
        uvage.pause()
    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
uvage.timer_loop(ticks_per_second, tick)
