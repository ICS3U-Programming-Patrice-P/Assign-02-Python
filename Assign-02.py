#!/usr/bin/env python3
# Created by: Patrice Pat-Odita
# Created on: Oct 1, 2022
# This program asks the user for the unit, length, height and
# width of a cube. It then
# calculates and displays the surface area and
# volume.
import math
 
 
def main():
    # input
    print("Today we will calculate the surface area and")
    print("volume of a cube")
    unit = (input("\033[1;35;34mEnter the units:"))
    length = int(input("\033[1;35;35mEnter the length:"))
    width = int(input("\033[1;35;36mEnter the width:"))
    height = int(input("\033[1;35;34mEnter the height:"))
 
 # process
    surface_area = int (6 * (length ^ 2))
    volume = (length * width * height)
 
    # output
    print("")
    print("\033[1;35;36mSurface Area ={:.2f} {}^2". format(surface_area, unit))
    print("\033[1;35;38mVolume ={:.2f} {}^3". format(volume, unit))
   
if __name__ == "__main__":
    main()
 
