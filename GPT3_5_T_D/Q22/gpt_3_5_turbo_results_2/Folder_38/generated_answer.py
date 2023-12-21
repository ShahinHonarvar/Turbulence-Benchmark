
def find_sum_of_multiples(n):
    multiples = [i for i in range(n, n*78, n)]
    return sum(multiples[:77])
