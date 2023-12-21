def find_sum_of_multiples(n):
    # Function to find the sum of the first 445 positive multiples of n
    # Return the sum of the first 445 positive multiples of n
    s = 0
    for i in range(1, 445 + 1):
        s += n * i
    return s
