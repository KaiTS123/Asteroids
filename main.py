import pygame
import vectors

playerShip = {
    "points": [
        {"x": 0, "y": -10},
        {"x": -10, "y": 10},
        {"x": 10, "y": 10},
        {"x": 0, "y": -10}
    ],
    "position": {"x": 100, "y": 100},
    "rotation": 0
}


def main():
    pygame.init()
    pygame.display.set_caption("Asteroids")

    pygame.font.init()
    fontArial = pygame.font.SysFont('Arial', 16)

    screen = pygame.display.set_mode((500, 500))

    running = True

    frameCount = 0

    while running:
        pygame.time.Clock().tick(60)

        screen.fill((0, 0, 0))

        frameCount += 1
        # textSurface = fontArial.render('frame = ' + str(frameCount), False, (255, 255, 255))
        # screen.blit(textSurface, (0, 0))

        playerShip["rotation"] += 0.01

        vectors.drawShape(screen, playerShip)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
