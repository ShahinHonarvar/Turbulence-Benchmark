
def find_sum_of_multiples(n):
    multiples = [i for i in range(n, 365*n, n)]
    return sum(multiples[:73])
