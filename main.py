import pygame
import vectors
from PlayerShip import PlayerShip

playerShip = PlayerShip()


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

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerShip.rotateLeft()
        if keys[pygame.K_RIGHT]:
            playerShip.rotateRight()
        if keys[pygame.K_UP]:
            playerShip.thrustForward()

        playerShip.draw(screen)
        playerShip.update()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
