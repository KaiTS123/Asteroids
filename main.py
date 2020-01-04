import pygame
import VectorShapes
from PlayerShip import PlayerShip
from Asteroid import Asteroid
from GameSettings import GameSettings


def checkInput(playerShip):
    # check keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerShip.rotateLeft()
    if keys[pygame.K_RIGHT]:
        playerShip.rotateRight()
    if keys[pygame.K_UP]:
        playerShip.thrustForward()
    if keys[pygame.K_SPACE]:
        playerShip.shootBullet()


def generateAsteroids(asteroids):
    asteroids.clear()
    for i in range(0, GameSettings.num_asteroids):
        asteroids.append(Asteroid())


def main():
    # game data
    playerShip = PlayerShip()

    asteroids = []
    generateAsteroids(asteroids)

    # initialise pygame
    pygame.init()
    pygame.display.set_caption("Asteroids")

    pygame.font.init()
    fontArial = pygame.font.SysFont('Arial', 16)

    screen = pygame.display.set_mode((GameSettings.screenSize["x"], GameSettings.screenSize["y"]))

    GameSettings.running = True

    frameCount = 0

    # main loop
    while GameSettings.running:
        # set frame rate
        pygame.time.Clock().tick(60)

        # fill screen with black
        screen.fill((0, 0, 0))

        # frame counter
        frameCount += 1
        # textSurface = fontArial.render('frame = ' + str(frameCount), False, (255, 255, 255))
        # screen.blit(textSurface, (0, 0))

        checkInput(playerShip)

        playerShip.draw(screen)
        playerShip.update()

        for index, asteroid in enumerate(asteroids):
            if VectorShapes.shapesColliding(asteroid, playerShip):
                playerShip.reset()
            asteroid.move()
            asteroid.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameSettings.running = False


if __name__ == "__main__":
    main()
