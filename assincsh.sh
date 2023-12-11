#!/bin/bash

# Define the number of iterations
iterations=10

# Start the loop
for i in $(seq 1 $iterations); do
  # Call the script asynchronously
  ./teste_1.sh &
done

# Wait for all background processes to finish
wait