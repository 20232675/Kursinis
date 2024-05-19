import pygame
import time

class GameObject:
    def __init__(self, image_path, x, y, width, height):
        self._image = pygame.image.load(image_path).convert_alpha()
        self._image = pygame.transform.scale(self._image, (width, height))
        self._rect = self._image.get_rect()
        self._rect.x = x
        self._rect.y = y

    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect

class Player(GameObject):
    def __init__(self, x, y):
        super().__init__('Pictures/skyn.png', x, y, 60, 80)
        self._jump = False
        self._jump_height = 10

    def jump_action(self):
        keys = pygame.key.get_pressed()
        if not self._jump and keys[pygame.K_SPACE]:
            self._jump = True

        if self._jump:
            if self._jump_height >= -10:
                if self._jump_height > 0:
                    self.rect.y -= (self._jump_height ** 2) / 2
                else:
                    self.rect.y += (self._jump_height ** 2) / 2
                self._jump_height -= 1
            else:
                self._jump = False
                self._jump_height = 10

class Enemy(GameObject):
    def __init__(self, x, y):
        super().__init__('Pictures/games.png', x, y, 60, 80)

def main():
    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((600, 300))
    pygame.display.set_caption("Run Sonic, run!")

    background = pygame.image.load('Pictures/background.webp').convert_alpha()
    background_size = pygame.transform.scale(background, (600, 330))

    icon = pygame.image.load('Pictures/motoroleris.png').convert_alpha()
    pygame.display.set_icon(icon)

    ghost_list_in_game = []
    background_x = 0

    player = Player(180, 180)
    # enemy = Enemy(610, 160)

    game_over_font = pygame.font.Font(None, 36)
    game_over_text = game_over_font.render("Game Over!", True, (255, 255, 255))
    game_over_rect = game_over_text.get_rect(center=(300, 150))

    running = True
    gameplay = True
    # jump_hight = 10

    ghost_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(ghost_timer, 1000)

    start_time = time.time()

    while running:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not gameplay:
                gameplay = True
                player.rect.y = 180
                ghost_list_in_game = []

            if event.type == ghost_timer and gameplay:
                ghost_list_in_game.append(Enemy(620, 160))

        if gameplay:
            player.jump_action()

            for ghost in ghost_list_in_game:
                ghost.rect.x -= 10
                if player.rect.colliderect(ghost.rect):
                    gameplay = False

            background_x -= 1
            if background_x == -600:
                background_x = 0

        screen.blit(background_size, (background_x, 0))
        screen.blit(background_size, (background_x + 600, 0))
        screen.blit(player.image, player.rect)
        for ghost in ghost_list_in_game:
            screen.blit(ghost.image, ghost.rect)

        if not gameplay:
            screen.fill((255, 0, 0))
            screen.blit(game_over_text, game_over_rect)

        pygame.display.update()
        clock.tick(60)

    end_time = time.time()
    runtime = end_time - start_time

    with open('execution_time.txt', 'w') as file:
        file.write(f"Program runtime: {runtime:.2f} seconds")

    pygame.quit()

if __name__ == "__main__":
    main()

