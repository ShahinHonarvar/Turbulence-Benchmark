
def find_sum_of_multiples(n):
    multiples = [i for i in range(n, n*132, n)]
    return sum(multiples)
