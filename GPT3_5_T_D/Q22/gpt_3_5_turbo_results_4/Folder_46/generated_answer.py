
def find_sum_of_multiples(n):
    multiples = [i * n for i in range(1, 465)]
    return sum(multiples)
