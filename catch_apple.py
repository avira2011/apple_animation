import pygame
import pgzrun
import random

WIDTH = 800
HEIGHT = 600

apple = Actor('apple')
basket = Actor('basket')

basket.x = 500
basket.y = 500

def draw():
    screen.clear()
    screen.blit('bg.webp', (0,0))

    apple.draw()
    basket.draw()

def place_apple():
    apple.y = 50
    apple.x = random.randint (50, 750)

def update():
    if keyboard.left:
        basket.x -= 5
    if keyboard.right:
        basket.x += 5
    apple.y += 2

    apple_catch = basket.colliderect(apple)
    if apple_catch:
        place_apple()
    if apple.y > 600:
        place_apple()
pgzrun.go()