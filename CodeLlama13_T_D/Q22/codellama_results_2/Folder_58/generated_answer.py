
def find_sum_of_multiples(n):
    return sum(i for i in range(1, 223*n+1) if i % n == 0)
