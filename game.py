'''
Elijah Kim - cys8qu
Jonah Lee - wkx9ff

Game Description: Space Invaders - player has to avoid falling obstacles, if timer runs out the player loses,
 player ship shoots projectiles at big enemy ship, player has a health bar and "Game Over" occurs if player loses all of them, 

Basic Features:
User Input - player will use keyboard arrow keys, can move left and right, up arrow will shoot projectiles
Game Over - "Game Over" screen will be shown once the player loses all 3 lives
Graphics/Images - projectiles will be blue squares, enemy will be one giant red square, player ship will be an image

Additional Features:
Restart from Game Over - player can choose to restart the game once they lose all of their lives. Their score will be reset.
Enemies - big square will move sporadically side to side, has a giant health bar which when depleted will end the game.
    enemy will shoot projectiles that the player has to avoid
Timer - once timer runs out, the player loses. Will be a number in the corner of the screen that ticks down
Health Bar - health bar depletes by a third each time the player is hit by an enemy projectile

'''

#EVERYTHING BELOW IS CHANGED FROM THE LAST SUBMISSION

import uvage

camera = uvage.Camera(600, 800)

player = uvage.from_color(300,700, "red", 40, 40)
enemy_ship = uvage.from_color(300, 100, "white", 150, 100)

left_border = uvage.from_color(0, 400, 'black', 1, 800)
right_border = uvage.from_color(600, 400, 'black', 1, 800)

proj = uvage.from_color(1000 , 1000, 'blue', 20, 20)

#ENEMY-HEALTH
enemy_health = 450
health_bar_g = uvage.from_color(300, 25, "green", enemy_health, 15)
health_bar_r = uvage.from_color(300, 25, "red", 450, 15)

#PLAYER-HEALTH
player_health = 450
p_health_bar_g = uvage.from_color(300, 775, "green", player_health , 15)
p_health_bar_r = uvage.from_color(300, 775, "red", 450, 15)

enemy_ship.speedx = 7
proj.speedy = 0

seconds = 10
#camera.draw("Destroy the Alien ship before it explodes! Press Space to Continue", 20, "green", 300, 300)

game_over = False

def tick():
    global game_over, enemy_health, health_bar_g, player_health, p_health_bar_g, p_health_bar_r, seconds
    camera.clear('black')

    proj.move_speed()
    proj.speedy = -150

    if uvage.is_pressing("right arrow"):
        player.x += 10

    if uvage.is_pressing("left arrow"):
        player.x -= 10

    if uvage.is_pressing("space"):
        proj.y = player.y - 50
        proj.x = player.x

    if proj.touches(enemy_ship):
        proj.x = 1000
        proj.y = 1000
        proj.move_to_stop_overlapping(enemy_ship)
        enemy_health -= 45
        health_bar_g = uvage.from_color(300, 25, "green", enemy_health, 15)

    enemy_ship.move_speed()

    if enemy_ship.right_touches(right_border):
        enemy_ship.speedx = -enemy_ship.speedx
    if enemy_ship.left_touches(left_border):
        enemy_ship.speedx = -enemy_ship.speedx

    if enemy_health == 0:
        game_over = True
        camera.draw("You Won!", 144, "green", 300, 300)

    seconds -= 1/30

    if not game_over:
        camera.draw(player)
        camera.draw(enemy_ship)
        camera.draw(left_border)
        camera.draw(right_border)
        camera.draw(proj)
        camera.draw(health_bar_r)
        camera.draw(health_bar_g)
        camera.draw(p_health_bar_r)
        camera.draw(p_health_bar_g)
        camera.draw(uvage.from_text(enemy_ship.x, enemy_ship.y, str(round(seconds)), 100, "Red", bold=True))

    camera.display()

ticks_per_second = 30
uvage.timer_loop(ticks_per_second, tick)


