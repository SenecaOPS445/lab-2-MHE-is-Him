#!/usr/bin/env python3

# Author: Malik Hamilton-Edwards
# Author ID: mhamilton-edwards
# Date Created: 2025/01/23

import sys

# Check if a command-line argument was provided
if len(sys.argv) < 2:
    print("Error: Please provide a number as an argument.")
    sys.exit(1)

# Assign the value of the first argument to the timer variable, converting it to an integer
timer = int(sys.argv[1])

# While loop to countdown from the provided number
while timer > 0:
    print(timer)
    timer -= 1  # Decrement the timer by 1

# Print 'blast off!' when the loop finishes
print("blast off!")
