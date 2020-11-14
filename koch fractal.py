#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:58:28 2020

@author: MTMC
"""

import turtle

def koch_fract(turtle, divis, size):
    if divis == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_fract(turtle, divis - 1, size / 3)
            turtle.left(angle)

divis = 7
size = 750

wn = turtle.Screen()
wn.setup(width=1000, height=500)

turtle.penup()
turtle.goto(-500, 150)

turtle.speed(100)
            
turtle.pendown()

for i in range(0, 3):
    koch_fract(turtle, divis, size)
    turtle.left(-120)
