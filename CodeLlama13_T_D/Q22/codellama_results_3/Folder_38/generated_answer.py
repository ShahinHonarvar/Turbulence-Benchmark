
def find_sum_of_multiples(n):
    return sum(i for i in range(1, 78) if i % n == 0)
