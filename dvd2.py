import uvage

width = 1000
height = 800
size = 150
camera = uvage.Camera(width, height)
dvd = uvage.from_text(400, 300, "DVD", size, "red")
colors = ["red", "blue", "green", "orange", "purple", "light blue", "yellow"]
speedx = 7
speedy = 5
idx = 0

def change_color():
    global dvd, size, idx, colors
    idx += 1
    if idx > len(colors) - 1:
        idx = 0
    dvd = uvage.from_text(dvd.x, dvd.y, "DVD", size, colors[idx])

def move():
    global dvd, speedy, speedx
    dvd.x += speedx
    dvd.y += speedy
    change_bound_black()

def change_bound_black():
    global dvd, speedy, speedx, width, height
    if dvd.left < 0 or dvd.right > width:
        speedx *= -1
        change_color()
    if dvd.top < -8 or dvd.bottom > height + 20:
        speedy *= -1
        change_color()

def tick():
    camera.clear("black")
    camera.draw(dvd)
    move()
    camera.display()

uvage.timer_loop(30, tick)