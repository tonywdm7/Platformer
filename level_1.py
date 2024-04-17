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

    portal_img = pygame.image.load("portal.png")
    heart_img = pygame.image.load("heart.png")

    class Portal(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = portal_img
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def draw(self, screen):
            screen.blit(self.image, self.rect)

    class Heart(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = heart_img
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y


        def draw(self, screen):
            screen.blit(self.image, self.rect)

    hearts = [Heart(10, 10), Heart(40, 10), Heart(70, 10)]
    portal = Portal(380, 50)

    health = 3
    spawn_position = (100, 50)

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for plt in platforms:
            if plt.collision_check(player_rect):
                player_center = player_rect.center
                platform_center = plt.rect.center
                dx = abs(player_center[0] - platform_center[0])
                dy = abs(player_center[1] - platform_center[1] - 100)
                if dx <= dy:
                    if -dy <= 0:
                        collide_check = True

                    break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            player_rect.x += player_speed
        if keys[pygame.K_a]:
            player_rect.x -= player_speed

        if not jumping:
            if keys[pygame.K_SPACE] and collide_check:
                jumping = True
                player_rect.y -= jump_speed
        else:
            player_rect.y -= jump_speed
            jump_speed -= 1
            if jump_speed == 0:
                jumping = False
                jump_speed = 15

        if player_rect.y > SCREEN_HEIGHT:
            hearts.pop(-1)
            health -= 1
            player_rect.topleft = spawn_position

        if health == 0:
            running = False

        if portal.rect.colliderect(player_rect):
            running = False

        if not collide_check and jump_speed >= 0:
            player_rect.y += gravity

        screen.blit(background, (0, 0))
        screen.blit(player_image, player_rect)
        for plt in platforms:
            plt.draw(screen)

        for h in hearts:
            h.draw(screen)

        portal.draw(screen)


        collide_check = False
        pygame.display.update()
        pygame.time.Clock().tick(60)

