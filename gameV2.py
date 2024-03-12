'''
Elijah Kim - cys8qu
Jonah Lee - wkx9ff

Game Description: Space Invaders - player has to enemy projectiles, if timer runs out the player loses,
 player ship shoots projectiles at big enemy ship, player has a health bar and "Game Over" occurs if player loses all of their health

Basic Features:
User Input - player will use keyboard arrow keys, can move left and right, space bar will shoot projectiles, press "S" to start
Game Over - "Game Over" screen will be shown once the player gets hit three times by enemy projectiles
Graphics/Images - player projectiles will be blue squares, enemy projectiles will be red squares, player ship and enemy ship will be images

Additional Features:
Restart from Game Over - player can choose to restart the game once they lose all of their lives..
Enemies - enemy ship will move side to side, has a giant health bar which when depleted will end the game.
    enemy will shoot projectiles that the player has to avoid
Timer - once timer runs out, the player loses. Will be a number (15 seconds) in the corner of the screen that ticks down
Health Bar - health bar depletes by a third each time the player is hit by an enemy projectile

'''

# EVERYTHING BELOW IS CHANGED FROM THE LAST SUBMISSION

import uvage

camera = uvage.Camera(600, 800)

# PLAYER AND ENEMY SHIP
player = uvage.from_image(300, 700, "SpaceShipCutOutv2.png")
enemy_ship = uvage.from_image(300, 115, "AlienSpaceship.png")

# BORDERS
left_border = uvage.from_color(0, 400, 'black', 1, 800)
right_border = uvage.from_color(600, 400, 'black', 1, 800)

# PLAYER PROJECTILE
proj = uvage.from_color(1000, 1000, 'blue', 20, 20)

#  ENEMY PROJECTILE
proj_enemy1, proj_enemy2, = uvage.from_color(1500, 1000, 'red', 20, 35), uvage.from_color(1200, 1000, 'red', 20, 35)

# ENEMY-HEALTH
enemy_health = 450
health_bar_g = uvage.from_color(300, 25, "green", enemy_health, 15)
health_bar_r = uvage.from_color(300, 25, "red", 450, 15)

# PLAYER-HEALTH
player_health = 450
health_bar_g2 = uvage.from_color(300, 775, "green", player_health, 15)
health_bar_r2 = uvage.from_color(300, 775, "red", 450, 15)

# SPEEDS
enemy_ship.speedx = 7
proj_enemy1.speedy = 0
proj_enemy2.speedy = 0
proj.speedy = 0

# GAME LOGISTICS
game_over = False
game_on = False
pressed_start = True  # This variable is so the player can't reset the enemy's health mid-game
game_start = False
counter = 30
when_enemy_fires = 0

# TIMER
timer = 100


def tick():
    global game_over, game_on, enemy_health, health_bar_g, player_health, health_bar_r2, health_bar_g2, timer, pressed_start, counter, game_start, when_enemy_fires
    camera.clear('black')

    proj.move_speed()
    proj_enemy1.move_speed()
    proj_enemy2.move_speed()

    proj.speedy = -150
    proj_enemy1.speedy = 100
    proj_enemy2.speedy = 100

    if not game_start:  # Before the game starts text
        camera.draw("Defeat the alien ship", 72, "green", 300, 200)
        camera.draw("before time runs out!", 72, "green", 300, 300)
        camera.draw("Press the arrow keys to move.", 55, "green", 300, 450)
        camera.draw("Press \"Space\" to Shoot!", 55, "green", 300, 550)
        camera.draw("Press \"S\" to Start!", 72, "red", 300, 650)

    if uvage.is_pressing("s") and pressed_start:  # Starts game if pressing "s" and pressed_start is True
        game_on = True
        game_start = True
        enemy_health = 450
        player_health = 450
        timer = 15
        health_bar_g = uvage.from_color(300, 25, "green", enemy_health, 15)
        health_bar_g2 = uvage.from_color(300, 775, "green", 450, 15)

    if game_on:  # Everything runs
        pressed_start = False
        counter -= 1
        camera.draw(player)
        camera.draw(enemy_ship)
        camera.draw(left_border)
        camera.draw(right_border)
        camera.draw(proj)
        camera.draw(proj_enemy1)
        camera.draw(proj_enemy2)
        camera.draw(health_bar_r)
        camera.draw(health_bar_g)
        camera.draw(health_bar_r2)
        camera.draw(health_bar_g2)
        camera.draw(uvage.from_text(30, 25, str(timer), 45, "Red", bold=True))  # Draws Timer

        if uvage.is_pressing("right arrow"):  # Player movement right
            player.x += 10

        if uvage.is_pressing("left arrow"):  # Player movement left
            player.x -= 10

        if uvage.is_pressing("space"):  # Player shoots projectile
            proj.y = player.y - 50
            proj.x = player.x

        if proj.touches(enemy_ship):  # Player projectile movement and collision with enemy ship
            proj.x = 1000
            proj.y = 1000
            proj.move_to_stop_overlapping(enemy_ship)
            enemy_health -= 45
            health_bar_g = uvage.from_color(300, 25, "green", enemy_health, 15)

        if proj_enemy1.touches(player) or proj_enemy2.touches(player):  # Enemy projectile movement and collision with player
            proj_enemy1.x = 1500
            proj_enemy1.y = 1500
            proj_enemy2.x = 1500
            proj_enemy2.y = 1500

            proj_enemy1.move_to_stop_overlapping(player)
            proj_enemy2.move_to_stop_overlapping(player)

            player_health -= 150
            health_bar_g2 = uvage.from_color(300, 775, "green", player_health, 15)

    enemy_ship.move_speed()

    '''Enemy ship bounces against walls of screen'''
    if enemy_ship.right_touches(right_border):
        enemy_ship.speedx = -enemy_ship.speedx
    if enemy_ship.left_touches(left_border):
        enemy_ship.speedx = -enemy_ship.speedx

    if enemy_health == 0:  # Win condition
        game_over = True
        game_on = False
        camera.draw("You Won!", 72, "green", 300, 300)
        camera.draw("The aliens won't be coming", 55, "green", 300, 375)
        camera.draw("back anytime soon.", 55, "green", 300, 450)
        camera.draw("Press \"S\" to Play Again!", 65, "green", 300, 600)
        pressed_start = True

    if player_health == 0:  # Lose condition #1 (when player_health drops to 0)
        game_over = True
        game_on = False
        camera.draw("Game Over!", 70, "red", 300, 300)
        camera.draw("Press \"S\" to Try Again!", 72, "green", 300, 450)
        pressed_start = True

    if when_enemy_fires == 2:  # Dictates when the enemy fires (every 3 seconds)
        proj_enemy1.y = enemy_ship.y + 50
        proj_enemy2.y = enemy_ship.y + 50
        proj_enemy1.x = enemy_ship.x - 30
        proj_enemy2.x = enemy_ship.x + 30
        when_enemy_fires = 0

    if counter == 0:  # Timer decreases by 1 every second
        timer -= 1
        counter = 30
        when_enemy_fires += 1
    if timer == 0:  # Lose condition #2 (time runs out)
        game_over = True
        game_on = False
        camera.draw("Time's Up! Game Over!", 70, "red", 300, 300)
        camera.draw("Press \"S\" to Start!", 72, "green", 300, 450)
        pressed_start = True

    camera.display()


ticks_per_second = 30

uvage.timer_loop(ticks_per_second, tick)