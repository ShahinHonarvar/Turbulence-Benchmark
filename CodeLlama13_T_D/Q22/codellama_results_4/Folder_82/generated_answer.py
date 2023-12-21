
def find_sum_of_multiples(n):
    return sum(range(1, 34) if x % n == 0 else range(1, 34) for x in range(1, 34))
