
def find_sum_of_multiples(n):
    return sum(range(1, 55) if i % n == 0 else 0 for i in range(1, 55))
