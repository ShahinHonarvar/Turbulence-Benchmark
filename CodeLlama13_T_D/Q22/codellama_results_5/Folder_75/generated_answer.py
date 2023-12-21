
def find_sum_of_multiples(n):
    return sum(range(1, 16) if i % n == 0 else range(1, 15) for i in range(1, 16))
