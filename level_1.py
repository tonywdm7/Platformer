def start_level1():
    import pygame
    import sys
    pygame.init()

    pygame.mixer.music.load("yeat.mp3")

    WHITE = (255, 255, 255)
    SCREEN_WIDTH = 420
    SCREEN_HEIGHT = 250

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Простая игра на Pygame")

    platform_img = pygame.image.load("platform.png")
    background = pygame.image.load("background.png")

    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    player_image = pygame.image.load("player.png")
    player_image = pygame.transform.scale(player_image, (player_image.get_width() * 2, player_image.get_height() * 2))

    player_rect = player_image.get_rect()
    player_rect.topleft = (100, 50)

    class Platform(pygame.sprite.Sprite):
        def __init__(self, x, y, width, height, image_path):
            super().__init__()
            self.image = image_path
            self.image = pygame.transform.scale(self.image, (width, height))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            # self.rect = (x, y)
            self.hitbox = pygame.Rect(self.rect.x, self.rect.y, width, height)

        def draw(self, screen):
            screen.blit(self.image, self.rect)

        def collision_check(self, player_rect):
            return self.hitbox.colliderect(player_rect)

    platforms = []
    def add_platform(x, y, width, height):
        Anton = Platform(x, y, width, height, platform_img)
        platforms.append(Anton)

    add_platform(10, 200, 175, 25)
    add_platform(200, 150, 175, 25)

    collide_check = False
    gravity = 5
    jump_speed = 15
    player_speed = 3
    jumping = False
    running = True

    pygame.mixer.music.play(-1)

    while running:





        screen.blit(background, (0, 0))
        screen.blit(player_image, player_rect)
        for plt in platforms:
            plt.draw(screen)

        pygame.display.update()

