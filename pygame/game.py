import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Initialize the mixer
pygame.mixer.init()

# Load Sound Stuff
wing_sound = pygame.mixer.Sound("sounds/wing_sound.mp3")
die_sound = pygame.mixer.Sound("sounds/die_sound.mp3")
point_sound = pygame.mixer.Sound("sounds/point_sound.mp3")

# Load background music
background_sound = pygame.mixer.SoundType("sounds/background.mp3")
pygame.mixer.music.load("sounds/background.mp3") 
pygame.mixer.music.set_volume(0.1)            
pygame.mixer.music.play(loops=-1)             

# Screen Stuff
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Clock and FPS 
clock = pygame.time.Clock()
FPS = 60

# Colors stuff for drawing
WHITE = (255, 255, 255)

# Font for score and lives
FONT = pygame.font.SysFont('Arial', 30, bold=True)

# Load images 
BIRD_SPRITE_SHEET = pygame.transform.scale(pygame.image.load("images/CS1110_BirdSprite.png"), (200, 70)) 
PIPE_IMG = pygame.transform.scale(pygame.image.load("images/CS1110_MarioPipe.png"), (80, 500))
PIPE_IMG_REV = pygame.transform.flip(PIPE_IMG, False, True) 
BG_IMG = pygame.transform.scale(pygame.image.load("images/background.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load life icon image
LIFE_ICON_IMG = pygame.image.load("images/life.png") 
LIFE_ICON_SIZE = 50
LIFE_ICON_IMG = pygame.transform.scale(LIFE_ICON_IMG, (LIFE_ICON_SIZE, LIFE_ICON_SIZE))

# Load custom font
FONT_PATH = "font.ttf"
SCORE_FONT_SIZE = 50
LIVES_FONT_SIZE = 50
SCORE_FONT = pygame.font.Font(FONT_PATH, SCORE_FONT_SIZE)
LIVES_FONT = pygame.font.Font(FONT_PATH, LIVES_FONT_SIZE)


# Bird class
class Bird:
    def __init__(self):
        self.frames = self.slice_sprite_sheet(BIRD_SPRITE_SHEET, 4)  
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(100, SCREEN_HEIGHT // 2))
        self.velocity = 0
        self.gravity = 0.5
        self.flap_speed = 5
        self.flap_counter = 0

    def slice_sprite_sheet(self, sprite_sheet, num_frames):
        frame_width = sprite_sheet.get_width() // num_frames
        frame_height = sprite_sheet.get_height()
        frames = [sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
                  for i in range(num_frames)]
        return frames

    def update(self):
        # Flapping animation
        self.flap_counter = (self.flap_counter + 1) % self.flap_speed
        if self.flap_counter == 0:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

        # Bird physics stuff
        self.velocity += self.gravity
        self.rect.y += int(self.velocity)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    # jump and jump height
    def jump(self):
        self.velocity = -10 

    def draw(self):
        screen.blit(self.image, self.rect)

# Pipe class
class Pipe:
    GAP = 200
    VELOCITY = 5
    MOVEMENT_RANGE = 100
    MOVEMENT_SPEED = 1

    def __init__(self, x, moving=False):
        self.x = x
        self.moving = moving
        self.moving_up = True
        self.height = 0
        self.top_pos = 0
        self.bottom_pos = 0
        self.PIPE_TOP = PIPE_IMG_REV
        self.PIPE_BOTTOM = PIPE_IMG
        self.passed = False
        self.set_height()
        self.movement_counter = 0

    def set_height(self):
        self.height = random.randrange(50, 300)
        self.top_pos = self.height - self.PIPE_TOP.get_height()
        self.bottom_pos = self.height + self.GAP

    def move(self):
        self.x -= self.VELOCITY
        if self.moving:
            if self.moving_up:
                self.top_pos -= self.MOVEMENT_SPEED
                self.bottom_pos -= self.MOVEMENT_SPEED
                self.movement_counter += self.MOVEMENT_SPEED
                if self.movement_counter >= self.MOVEMENT_RANGE:
                    self.moving_up = False
            else:
                self.top_pos += self.MOVEMENT_SPEED
                self.bottom_pos += self.MOVEMENT_SPEED
                self.movement_counter -= self.MOVEMENT_SPEED
                if self.movement_counter <= -self.MOVEMENT_RANGE:
                    self.moving_up = True

    def draw(self):
        screen.blit(self.PIPE_TOP, (self.x, self.top_pos))
        screen.blit(self.PIPE_BOTTOM, (self.x, self.bottom_pos))

    def collide(self, bird):
        bird_mask = pygame.mask.from_surface(bird.image)
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.rect.left, self.top_pos - round(bird.rect.top))
        bottom_offset = (self.x - bird.rect.left, self.bottom_pos - round(bird.rect.top))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if b_point or t_point:
            return True
        return False

def draw_text_with_outline(text, font, color, outline_color, surface, x, y, outline_width):
    base = font.render(text, True, color)
    outline = font.render(text, True, outline_color)

    # Render text outline
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            surface.blit(outline, (x + dx, y + dy))

    # Render base text
    surface.blit(base, (x, y))

def draw_lives(lives, icon_img, surface, start_x, y, padding=5):
    for i in range(lives):
        surface.blit(icon_img, (start_x + i * (icon_img.get_width() + padding), y))

def main():
    bird = Bird()
    pipes = [Pipe(700)]
    score = 0
    lives = 3
    run = True
    level = 1
    invincibility_timer = 0

    while run:
        if score > 15 and level == 1:
            level = 2
            pygame.mixer.music.load("sounds/background_2.mp3")  
            pygame.mixer.music.set_volume(0.2)    
            pygame.mixer.music.play(-1)  

        clock.tick(FPS)
        screen.blit(BG_IMG, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    bird.jump()
                    wing_sound.play() 

        bird.update()
        bird.draw()

        if invincibility_timer > 0:
            invincibility_timer -= 1

        rem = []
        add_pipe = False
        for pipe in pipes:
            if pipe.collide(bird) and invincibility_timer == 0:
                lives -= 1
                invincibility_timer = FPS * 2  # 2 seconds of invincibility

                die_sound.play()

                if lives == 0:
                    run = False
                    
            if not pipe.passed and pipe.x < bird.rect.x:
                pipe.passed = True
                add_pipe = True
                score += 1  
                point_sound.play()

            pipe.move()
            pipe.draw()

            # Remove pipes that have gone off screen
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

        # Generate new pipes
        if add_pipe:
            if score > 15:  # Start moving pipes after score reaches 20
                pipes.append(Pipe(SCREEN_WIDTH, moving=True)) 
            else:
                pipes.append(Pipe(SCREEN_WIDTH))
        for r in rem:
            pipes.remove(r)

        # Draw score and lives
        draw_text_with_outline(f'Score: {score}', SCORE_FONT, WHITE, (0, 0, 0), screen, 20, 20, 2)
        draw_lives(lives, LIFE_ICON_IMG, screen, SCREEN_WIDTH - (lives * (LIFE_ICON_SIZE + 5)), 20)

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
