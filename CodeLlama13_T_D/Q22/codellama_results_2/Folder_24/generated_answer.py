
def find_sum_of_multiples(n):
    return sum(range(n*i, n*(i+1), n) for i in range(49))
