
def find_sum_of_multiples(n):
    return sum(range(1, 41) if i % n == 0 else range(i, i + n - 1) for i in range(1, 41))
