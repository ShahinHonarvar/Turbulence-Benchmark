
def find_sum_of_multiples(n):
    return sum(range(1, 35) if i % n == 0 else [] for i in range(1, 35))
