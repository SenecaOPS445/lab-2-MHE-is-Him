#!/usr/bin/env python3

# Author: Malik Hamilton-Edwards
# Author ID: mhamilton-edwards
# Date Created: 2025/01/23

import sys

# Check if a command-line argument was provided
if len(sys.argv) < 2:
    # Default timer value is 3 if no argument is provided
    timer = 3
else:
    # Convert the command-line argument to an integer and assign it to timer
    timer = int(sys.argv[1])

# While loop to countdown from the provided number or the default value
while timer > 0:
    print(timer)
    timer -= 1  # Decrement the timer by 1

# Print 'blast off!' when the loop finishes
print("blast off!")
