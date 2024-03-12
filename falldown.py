import uvage

camera = uvage.Camera(800, 600)

box1 = uvage.from_color(400,100,'red',40,40)
box1.speedx = 0

score = 0

platforms = [
uvage.from_color(600, 115, 'black', 500, 40), uvage.from_color(0, 115, 'black', 600, 40),
uvage.from_color(700, 300, 'black', 500, 40), uvage.from_color(0, 300, 'black', 800, 40),
uvage.from_color(900, 500, 'black', 500, 40), uvage.from_color(0, 500, 'black', 1200, 40)
]

top_layer = uvage.from_color(400, 1, 'black', 800, 1)

game_over = False

def tick():
	global game_over
	global score

	camera.clear('white')
	box1.move_speed()

	box1.speedy += 1

	if uvage.is_pressing("left arrow"):
		box1.x -= 10
	if uvage.is_pressing("right arrow"):
		box1.x += 10

	if box1.y > 590:
		box1.y = 590
	if box1.x > 780:
		 box1.x = 780
	if box1.x < 20:
		box1.x = 20

	for platform in platforms:
		camera.draw(platform)
		box1.move_to_stop_overlapping(platform)
		if not game_over:
			platform.y -= 3
			camera.draw(box1)
			score += 1
		if platform.y < 10:
			platform.y = 600
		if box1.touches(top_layer):
			game_over = True
			camera.draw("Game Over", 144, "blue", 400, 300)

	camera.draw(uvage.from_text(100, 50, str(score), 100, "Red", bold=True))

	camera.display()

	print(box1.x, box1.y, box1.speedx, box1.speedy)


uvage.timer_loop(30,tick)