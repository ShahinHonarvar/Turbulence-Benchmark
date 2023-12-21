def find_sum_of_multiples(n):
    # Create a list of all 73 multiples of n.
    multiples = []
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            multiples.append(j)
    # Return the sum of the list of multiples.
    return sum(multiples)
