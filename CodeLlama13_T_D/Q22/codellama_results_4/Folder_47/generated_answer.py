
def find_sum_of_multiples(n):
    return sum([x for x in range(1, 38*n+1) if not (x % n)])
