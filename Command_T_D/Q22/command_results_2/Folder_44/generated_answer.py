def find_sum_of_multiples(n):
    # Store the sum of the first 445 positive multiples of n in a variable
    # named 'sum'.
    sum = 0
    # Create a for loop that starts at 1 and ends at 445. Use the range() function
    # to create a range of numbers from start to stop.
    for i in range(1, 446):
        # Add i to the sum variable for every i in the range.
        sum += i * n
    # Return the sum variable.
    return sum
