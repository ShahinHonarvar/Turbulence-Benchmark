
def find_sum_of_multiples(n):
    return sum(range(1, 38) if i % n == 0 for i in range(1, 38))
