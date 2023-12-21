
def find_sum_of_multiples(n):
    return sum(i for i in range(1, 64*n+1, n))
