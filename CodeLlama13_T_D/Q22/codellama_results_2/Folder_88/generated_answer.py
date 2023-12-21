
def find_sum_of_multiples(n):
    return sum(i for i in range(1, 23*n+1) if not i % n)
