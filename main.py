import pygame
from level_1 import start_level1

WIDTH, HEIGHT = 420, 250
BUTTON_WIDTH, BUTTON_HEIGHT = 100, 50

BLACK = (0, 0, 0)

pygame.init()

click_sound = pygame.mixer.Sound("click.mp3")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

button_image = pygame.image.load("button_image.png")
button_image = pygame.transform.scale(button_image, (BUTTON_WIDTH, BUTTON_HEIGHT))

dark_button_image = pygame.image.load("dark_button_image.png")
dark_button_image = pygame.transform.scale(dark_button_image, (BUTTON_WIDTH, BUTTON_HEIGHT))

buttons = []

for i in range(1, 7):
    x = (i - 1) % 3 * (BUTTON_WIDTH + 10) + 50
    y = (i - 1) // 3 * (BUTTON_HEIGHT + 10) + 50

    button_rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
    buttons.append(button_rect)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, button in enumerate(buttons):
                    if button.collidepoint(event.pos):
                        click_sound.play()
                        print("hi")
                        level = i + 1
                        exec(f"start_level{level}()")

    screen.fill(BLACK)

    for i, button in enumerate(buttons):
        if button.collidepoint(pygame.mouse.get_pos()):
            screen.blit(dark_button_image, button)
        else:
            screen.blit(button_image, button)
        font = pygame.font.SysFont(None, 30)
        text = font.render(str(i + 1), True, BLACK)
        text_rect = text.get_rect(center=button.center)
        screen.blit(text, text_rect)

    pygame.display.flip()