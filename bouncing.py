import uvage

camera = uvage.Camera(800,600)

box1 = uvage.from_color(400,100,'black',20,20)


def tick():
	camera.clear('tan')
	box1.move_speed()

	camera.draw(box1)
	camera.display()
	#print(box1.x,box1.y,box1.speedx,box1.speedy)


uvage.timer_loop(30,tick)