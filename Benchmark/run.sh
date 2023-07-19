#!/bin/bash

# Set the number of iterations
iterations=10

# Set the Python program file
python_file="main.py"

# Run the Python program for the specified number of iterations
for ((i=1; i<=iterations; i++))
do
  echo "Iteration $i"

  # Run the Python program in a new shell
  python3 $python_file

  # Wait for the program to finish
  wait

  echo "Iteration $i completed."
done
