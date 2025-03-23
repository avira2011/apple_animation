import pgzrun
import pygame

WIDTH = 600
HEIGHT = 500

apple = Actor('apple')
apple.pos = (40,250)

def draw():
    screen.clear()
    apple.draw()

def animation():
    animate(apple, pos = (580, 250), duration = 5, on_finished = reverse_animation)

def reverse_animation():
    animate(apple, pos = (40,250), duration = 3)

animation() 

pgzrun.go()

