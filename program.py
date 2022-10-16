from tracemalloc import start
import pygame
import math
import time


screen = pygame.display.set_mode((500, 600))

running = 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

posX = 250
posY = 165

secs = 0
clockwiseLength = 300 - posY
totalTime = 0

while running:
    startTime = time.time()
    screen
    pygame.draw.circle(screen, WHITE, (250, 300), 150)
    pygame.draw.circle(screen, BLACK, (250, 300), 150 - 2)
    pygame.draw.line(screen, WHITE, (250, 300), (posX, posY))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
    period = time.time() - startTime
    totalTime += period
    if totalTime >= 1:
        secs += 1
        alpha = 6 * secs * math.pi / 180
        posX = 250 + clockwiseLength * math.sin(alpha)
        posY = 300 - clockwiseLength * math.cos(alpha)
        totalTime = 0
