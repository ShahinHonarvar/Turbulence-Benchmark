
def find_sum_of_multiples(n):
    # Find the sum of the first 28 positive multiples of n
    multiples = [n*i for i in range(1, 29)]
    return sum(multiples)
