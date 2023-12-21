
def find_sum_of_multiples(n):
    return sum([x for x in range(1, 472*n+1) if x % n == 0])
