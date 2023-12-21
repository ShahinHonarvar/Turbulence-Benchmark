
def find_sum_of_multiples(n):
    multiples = [x for x in range(n, n*36, n)]
    return sum(multiples)
