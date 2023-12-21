
def find_sum_of_multiples(n):
    multiples = [i * n for i in range(1, 79)]
    return sum(multiples)
