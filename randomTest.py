import random
import pygame
pygame.init()
errors = 0
for i in range(0, 10000):
    x = random.randint(1,99)*10
    y = random.randint(1,55)*10
    if x < 10 or x > 990 or y < 10 or y > 550:
        errors += 1
print(str(errors) + " errors out of 10000 tries")
print("which is " + str(errors/10000) + "%")
