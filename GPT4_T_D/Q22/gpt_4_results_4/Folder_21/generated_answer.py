
def find_sum_of_multiples(n):
    multiples = [n*i for i in range(1, 408)]
    return sum(multiples)
