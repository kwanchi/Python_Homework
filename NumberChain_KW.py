#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:16:27 2020

@author: willik37
"""
play = "y"
last_number = 0
while play == "y":
    x = int(input("How many numbers?"))
    x+=last_number  
    for i in range (last_number, x):
        # Debug code here
        print(f'{last_number}: last_number')
        print(f'{x}: x')
        # Note that you are incrementing last_number as you go, so it will eventually catch up to x and stop the loop
        last_number = last_number + 1
    play = input("Continue the chain: (y)es or (n)o?")
    if play == "n":
        break
    elif play == "y":
        continue
    else:
        play = input("Choose y or n! no other options")
        continue



    


