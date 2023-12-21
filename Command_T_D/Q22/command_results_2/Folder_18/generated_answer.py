def find_sum_of_multiples(n):
    # Take input from the user
    # Function to find the sum of the first 392 multiples of the given number
    # Start with 1 and end with (n//2)*2
    # Multiply each number by the given number and add to the running sum
    # Return the running sum
    return (n//2)*2*(n//2+1)
