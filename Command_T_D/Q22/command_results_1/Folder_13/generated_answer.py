def find_sum_of_multiples(n):
    return sum(range(1, min(n*2, 206) + 1, n))
