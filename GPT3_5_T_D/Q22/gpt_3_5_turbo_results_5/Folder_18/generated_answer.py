
def find_sum_of_multiples(n):
    multiples = [i * n for i in range(1, 393)]
    return sum(multiples)
