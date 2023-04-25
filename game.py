# Huy Nguyen - mpc5ya
# Theodore LengKong - fhd2bk

# Flappy Bird game project

# The objective of this game is to traverse through 2 levels, each level containing 20 pipes that jut from the ceiling
# and floor. The player must traverse through the 2 levels without dying. The bird has three lives, and every time it
# collides with a pipe, it loses one life. The game is designed similarly to Flappy Bird.

# Basic Feature 1 (User Input): The user input for this game consists of the up arrow keys and space bar.
# Pressing the up arrow key or space bar will make the bird fly up.

# Basic Feature 2 (Game Over): The game will end if the bird runs out of all its lives or completes both levels.

# Basic Feature 3 (Graphics/Images): The game incorporates images of Twitter Bird and Mario Pipes.

# Additional Feature 1 (Restart from Game Over): When the game ends, a screen will appear, stating "Press Space
# to Restart." The player can then restart the game again.

# Additional Feature 2 (Spite Animation): The bird will flap its wings.

# Additional Feature 3 (Enemies): In this game, the pipes serve as the enemies.
# If the bird collides with a pipe, it loses one life.

# Additional Feature 4 (Health Bar): The bird's health is shown through a health bar. Every time the bird touches a
# pipe, the bar will get shorter by 33%. Everytime it collides with a pipe, the bird gets teleported forward and the
# speed of the bird gets decreased

# Additional Feature 5 (Multiple Levels): The game has 2 levels. If the player is able to make it to 20 pipes on the
# first level, the player can proceed to level 2. In level 2, the pipes are moving instead of static pipes like in the
# first level.

import uvage
from random import randint

# Set the camera 800 x 600
camera = uvage.Camera(800, 600)

# Creates the Bird Character
bird_images = uvage.load_sprite_sheet("CS1110_BirdSprite.png", 1, 4)
current_frame = 0
bird = uvage.from_image(50, 300, bird_images[int(current_frame)])
bird.height = 40


# Creates the Sprite Flapping Animation for the bird
def loop_images():
    global bird, bird_images, current_frame
    current_frame += 0.6
    bird.image = bird_images[int(current_frame)]
    if current_frame >= len(bird_images) - 1:
        current_frame = 0


# all boundaries, pipes, and invisible lines/ areas (which will be used to track the position of the bird)
# invisible lines used to count score if the bird pass
# invisible area to be activated when the bird get hit to lower the speed by using bird.touches(invisible_area)
y_bottom1 = 800
y_bottom2 = 650
y_bottom3 = 500
pipe_bottom1 = uvage.from_image(200, y_bottom1, "CS1110_MarioPipe.png")
pipe_bottom1.height = 600
pipe_bottom2 = uvage.from_image(500, y_bottom2, "CS1110_MarioPipe.png")
pipe_bottom2.height = 600
pipe_bottom3 = uvage.from_image(800, y_bottom3, "CS1110_MarioPipe.png")
pipe_bottom3.height = 600
pipe_top1 = uvage.from_image(200, y_bottom1 - 750, "CS1110_MarioPipeRev.png")
pipe_top1.height = 600
pipe_top2 = uvage.from_image(500, y_bottom2 - 750, "CS1110_MarioPipeRev.png")
pipe_top2.height = 600
pipe_top3 = uvage.from_image(800, y_bottom3 - 750, "CS1110_MarioPipeRev.png")
pipe_top3.height = 600
invisible_line1 = uvage.from_color(200, 300, "tan", 2, 600)
invisible_line2 = uvage.from_color(500, 300, "tan", 2, 600)
invisible_line3 = uvage.from_color(800, 300, "tan", 2, 600)
invisible_area1 = uvage.from_color(50, 300, "tan", 50, 600)

# drawing health_bar
health_bar_length = 600
health_bar = uvage.from_color(0, 20, "red", health_bar_length, 20)

# Preset Conditions
game_start = False
game_over = False
win_game_1 = False
win_game_2 = False
before_touch = False
lv1 = False
lv2 = False

# physics
gravity = 0.8
pipe_speed_x = 2.5
pipe_speed_y = 1.25

# Use to count the score, depending on which invisible line the bird touches.
count = 0
touch_count1 = 0
touch_count2 = 0
touch_count3 = 0

# panels and background
background2 = uvage.from_image(400, 300, "CS1110_Background2.png")
background2.width = 1200
start_panel = uvage.from_text(400, 300, "Press ENTER to start Level 1", 50, "red")
end_panel1 = uvage.from_text(400, 250, "Game over, you got " + str(count) + " points", 50, "red")
end_panel2 = uvage.from_text(400, 300, "Press R to play again", 50, "red")
win_panel = uvage.from_text(400, 250, "Congratulations! You Won!", 50, "red")
next_panel = uvage.from_text(400, 350, "or Press N to continue to Level 2", 50, "red")


# This function is implemented firstly to check if the user is pressing "Enter" to start the game
def start_game():
    global game_start, before_touch
    if uvage.is_pressing("return"):
        game_start = True
        before_touch = True


# Check if the player has crossed 20 pipes in Level 1
def win_1():
    global count, win_game_1
    if count == 20:
        win_game_1 = True


# Check if the player has crossed 20 pipes in Level 2
def win_2():
    global count, win_game_2
    if count == 20:
        win_game_2 = True


# Check if the player has died Level 1 or Level 2
def lose():
    global health_bar_length, game_over
    if health_bar_length == 0:
        game_over = True


# End game just update the score panel
def end_game():
    global end_panel1
    end_panel1 = uvage.from_text(400, 250, "Game over, you got " + str(count) + " point(s)", 50, "red")


# Check if the player are pressing R or N to continue to the next level, or play again
def play_again():
    global game_over, win_game_1, win_game_2, health_bar_length, count, lv2
    if uvage.is_pressing("r"):
        game_over = False
        win_game_1 = False
        win_game_2 = False
        lv2 = False
        reset()

    if uvage.is_pressing("n") and win_game_1:
        game_over = False
        win_game_1 = False
        win_game_2 = False
        lv2 = True
        reset()


# reset is called in play_again to redraw everything in their original position just like after starting the game
def reset():
    global count, health_bar_length
    global health_bar, bird, y_bottom1, y_bottom2, y_bottom3, pipe_bottom1, pipe_bottom2, pipe_bottom3, pipe_top1, pipe_top2, pipe_top3
    global invisible_line1, invisible_line2, invisible_line3, invisible_area1
    count = 0
    health_bar_length = 600
    y_bottom1 = 750
    health_bar = uvage.from_color(0, 20, "red", health_bar_length, 20)
    pipe_bottom1 = uvage.from_image(200, y_bottom1, "CS1110_MarioPipe.png")
    pipe_bottom1.height = 600
    pipe_bottom2 = uvage.from_image(500, y_bottom2, "CS1110_MarioPipe.png")
    pipe_bottom2.height = 600
    pipe_bottom3 = uvage.from_image(800, y_bottom3, "CS1110_MarioPipe.png")
    pipe_bottom3.height = 600

    pipe_top1 = uvage.from_image(200, y_bottom1 - 750, "CS1110_MarioPipeRev.png")
    pipe_top1.height = 600
    pipe_top2 = uvage.from_image(500, y_bottom2 - 750, "CS1110_MarioPipeRev.png")
    pipe_top2.height = 600
    pipe_top3 = uvage.from_image(800, y_bottom3 - 750, "CS1110_MarioPipeRev.png")
    pipe_top3.height = 600

    invisible_line1 = uvage.from_color(200, 300, "tan", 2, 600)
    invisible_line2 = uvage.from_color(500, 300, "tan", 2, 600)
    invisible_line3 = uvage.from_color(800, 300, "tan", 2, 600)

    invisible_area1 = uvage.from_color(50, 300, "tan", 50, 600)
    bird = uvage.from_image(50, 300, bird_images[int(current_frame)])
    bird.height = 40


# Puts boundaries on all sides of the camera so that the bird cannot pass through
def boundaries():
    global bird
    if bird.y > 580:
        bird.y = 580
        bird.speedy = 0
    if bird.x > 780:
        bird.x = 780
    if bird.x < 20:
        bird.x = 20
    if bird.y < 20:
        bird.y = 20


# Moves all the pipes and invisible line at a constant speed
def pipe_movement():
    global pipe_speed_x
    pipe_bottom1.speedx = -pipe_speed_x
    pipe_bottom2.speedx = -pipe_speed_x
    pipe_bottom3.speedx = -pipe_speed_x
    pipe_top1.speedx = -pipe_speed_x
    pipe_top2.speedx = -pipe_speed_x
    pipe_top3.speedx = -pipe_speed_x
    invisible_line1.speedx = -pipe_speed_x
    invisible_line2.speedx = -pipe_speed_x
    invisible_line3.speedx = -pipe_speed_x
    pipe_bottom1.move_speed()
    pipe_bottom2.move_speed()
    pipe_bottom3.move_speed()
    pipe_top1.move_speed()
    pipe_top2.move_speed()
    pipe_top3.move_speed()
    invisible_line1.move_speed()
    invisible_line2.move_speed()
    invisible_line3.move_speed()


# Allows for the pipe to move up and down in Level 2
def pipe_movement2():
    global pipe_speed_y
    global pipe_bottom1, pipe_bottom2, pipe_bottom3, pipe_top1, pipe_top2, pipe_top3
    global invisible_line1, invisible_line2, invisible_line3
    if (550 <= pipe_bottom3.y <= 750 and pipe_bottom3.speedy == 0) or pipe_bottom3.y < 550:
        pipe_bottom3.speedy = pipe_speed_y
        pipe_top3.speedy = pipe_speed_y
    if pipe_bottom3.y > 750:
        pipe_bottom3.speedy = -pipe_speed_y
        pipe_top3.speedy = -pipe_speed_y
    if (550 <= pipe_bottom2.y <= 750 and pipe_bottom2.speedy == 0) or pipe_bottom2.y < 550:
        pipe_bottom2.speedy = pipe_speed_y
        pipe_top2.speedy = pipe_speed_y
    if pipe_bottom2.y > 750:
        pipe_bottom2.speedy = -pipe_speed_y
        pipe_top2.speedy = -pipe_speed_y
    if (550 <= pipe_bottom1.y <= 750 and pipe_bottom1.speedy == 0) or pipe_bottom1.y < 550:
        pipe_bottom1.speedy = pipe_speed_y
        pipe_top1.speedy = pipe_speed_y
    if pipe_bottom1.y > 750:
        pipe_bottom1.speedy = -pipe_speed_y
        pipe_top1.speedy = -pipe_speed_y


# Allows the user to control the bird by pressing the up arrow or space button.
def bird_control():
    global bird, gravity
    bird.speedy += gravity
    if uvage.is_pressing('up arrow') or uvage.is_pressing("space"):
        bird.speedy = -7

# If the bird is touching the pipe, lower the speed of the game by setting the before_touch to True to trigger the
# lower_game_speed function
# Also increase the x_position of the bird to the right
def bird_touch_pipe():
    global health_bar_length, health_bar, before_touch
    global invisible_area1
    if pipe_bottom1.left_touches(bird) or pipe_bottom2.left_touches(bird) or pipe_bottom3.left_touches(bird):
        health_bar_length -= 200
        health_bar = uvage.from_color(0, 20, "red", health_bar_length, 20)
        bird.x += 150
        invisible_area1.x += 150
        before_touch = True
    if pipe_top1.left_touches(bird) or pipe_top2.left_touches(bird) or pipe_top3.left_touches(bird):
        health_bar_length -= 200
        health_bar = uvage.from_color(0, 20, "red", health_bar_length, 20)
        bird.x += 150
        invisible_area1.x += 150
        before_touch = True
    if pipe_bottom1.top_touches(bird) or pipe_bottom2.top_touches(bird) or pipe_bottom3.top_touches(bird):
        health_bar_length -= 200
        health_bar = uvage.from_color(0, 20, "red", health_bar_length, 20)
        bird.right += 125
        invisible_area1.right += 125
        before_touch = True
    if pipe_top1.bottom_touches(bird) or pipe_top2.bottom_touches(bird) or pipe_top3.bottom_touches(bird):
        health_bar_length -= 200
        health_bar = uvage.from_color(0, 20, "red", health_bar_length, 20)
        bird.right += 125
        invisible_area1.right += 125
        before_touch = True
    if health_bar_length == 0:
        end_game()


def draw_again():
    global y_bottom1, y_bottom2, y_bottom3, pipe_bottom1, pipe_bottom2, pipe_bottom3, pipe_top1, pipe_top2, pipe_top3
    global invisible_line1, invisible_line2, invisible_line3
    if pipe_bottom1.right < 0:
        y_bottom1 = randint(500, 800)
        pipe_bottom1 = uvage.from_image(850, y_bottom1, "CS1110_MarioPipe.png")
        pipe_bottom1.height = 600
        pipe_top1 = uvage.from_image(850, y_bottom1 - 750, "CS1110_MarioPipeRev.png")
        pipe_top1.height = 600
        invisible_line1 = uvage.from_color(850, 300, "tan", 2, 600)
    if pipe_bottom2.right < 0:
        y_bottom2 = randint(500, 800)
        pipe_bottom2 = uvage.from_image(850, y_bottom2, "CS1110_MarioPipe.png")
        pipe_bottom2.height = 600
        pipe_top2 = uvage.from_image(850, y_bottom2 - 750, "CS1110_MarioPipeRev.png")
        pipe_top2.height = 600
        invisible_line2 = uvage.from_color(825, 300, "tan", 2, 600)
    if pipe_bottom3.right < 0:
        y_bottom3 = randint(500, 800)
        pipe_bottom3 = uvage.from_image(850, y_bottom3, "CS1110_MarioPipe.png")
        pipe_bottom3.height = 600
        pipe_top3 = uvage.from_image(850, y_bottom3 - 750, "CS1110_MarioPipeRev.png")
        pipe_top3.height = 600
        invisible_line3 = uvage.from_color(850, 300, "tan", 2, 600)


# Increases the score by one whenever the bird crosses an invisible line
# Set the before_touch to "False" to set the game speed to its original speed
def score_counter():
    global touch_count1, touch_count2, touch_count3, count, before_touch
    camera.draw(uvage.from_text(750, 50, str(count), 70, "yellow"))

    # If the bird touches the invisible_line, the touch_count will go up really fast since it is touching multiple frames
    # touch_count is used to track the number of touches
    # When this number is one, which means that the bird has first touched the pipe in the first frame, we set the condition
    # to be true and increase the score by one. The touch_count can be increased to 2,3 or 4 due to multiple frames but
    # the score will not be increase anymore
    # After the bird completely pass the pipe gap, touch_count will be set to 0 for the next use after the pipe is drawn again
    if bird.touches(invisible_line1):
        before_touch = False
        touch_count1 += 1
        if touch_count1 == 1:
            count += 1
            camera.draw(uvage.from_text(750, 50, str(count), 70, "yellow"))
    else:
        touch_count1 = 0

    if bird.touches(invisible_line2):
        before_touch = False
        touch_count2 += 1
        if touch_count2 == 1:
            count += 1
            camera.draw(uvage.from_text(750, 50, str(count), 70, "yellow"))
    else:
        touch_count2 = 0

    if bird.touches(invisible_line3):
        before_touch = False
        touch_count3 += 1
        if touch_count3 == 1:
            count += 1
            camera.draw(uvage.from_text(750, 50, str(count), 70, "yellow"))
    else:
        touch_count3 = 0


# Lowers the speed of the pipe and the bird flapping whenever the bird hits a pipe
def lower_game_speed():
    global pipe_speed_x, before_touch, pipe_speed_y, current_frame
    if bird.touches(invisible_area1) and before_touch:
        pipe_speed_x = 1.25
        pipe_speed_y = 0.75
        current_frame -= 0.4
    else:
        pipe_speed_x = 2.5


def tick():
    global pipe_speed_x, game_start
    global game_over, win_game_1, win_game_2
    camera.clear("tan")
    camera.draw(background2)
    start_game()
    if not game_start:
        camera.draw(start_panel)
    elif game_start and not game_over and not win_game_1 and not win_game_2:
        camera.draw(invisible_line1)
        camera.draw(invisible_line2)
        camera.draw(invisible_line3)
        camera.draw(invisible_area1)
        camera.draw(background2)
        camera.draw(pipe_bottom1)
        camera.draw(pipe_bottom2)
        camera.draw(pipe_bottom3)
        camera.draw(pipe_top1)
        camera.draw(pipe_top2)
        camera.draw(pipe_top3)
        camera.draw(health_bar)
        camera.draw(bird)
        if lv2:
            pipe_movement2()
            win_2()
        loop_images()
        bird_control()
        bird.move_speed()
        boundaries()
        bird_touch_pipe()
        pipe_movement()
        score_counter()
        lower_game_speed()
        win_1()
        lose()
        draw_again()
    elif game_over:
        end_game()
        camera.draw(end_panel1)
        camera.draw(end_panel2)
        play_again()
    elif win_game_1:
        end_game()
        camera.draw(win_panel)
        camera.draw(end_panel2)
        camera.draw(next_panel)
        play_again()
    elif win_game_2:
        end_game()
        camera.draw(win_panel)
        camera.draw(end_panel2)
        camera.draw(next_panel)
        play_again()
    camera.display()

uvage.timer_loop(40, tick)