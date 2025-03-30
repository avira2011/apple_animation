import pgzrun
import pygame

WIDTH = 1300
HEIGHT = 800


bb = Actor('bb')
bb.pos = (40,250)

def draw():
    screen.clear()
    bb.draw()

def animation():
    animate(bb, pos = (1250, 400), duration = 5, on_finished = reverse_animation)

def reverse_animation():
    animate(bb, pos = (50,400), duration = 3)

animation()

pgzrun.go()

