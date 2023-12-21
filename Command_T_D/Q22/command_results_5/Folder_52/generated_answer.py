def find_sum_of_multiples(n):
    # Function to find the sum of the first 423 multiples of n
    # Your code here!
    s = 0
    for i in range(1, 423 + 1):
        s += n * i
    return s
