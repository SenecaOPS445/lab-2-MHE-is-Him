#!/usr/bin/env python3

import sys

# Check if the number of arguments is not equal to 2
if len(sys.argv) != 3:
    # Print usage message with the script name
    print(f"Usage: {sys.argv[0]} name age")
    # Exit with code 0 (successful execution, just indicating invalid arguments)
    sys.exit(0)

# Assign command-line arguments to variables
name = sys.argv[1]
age = sys.argv[2]

# Print the expected output
print(f"Hi {name}, you are {age} years old.")

