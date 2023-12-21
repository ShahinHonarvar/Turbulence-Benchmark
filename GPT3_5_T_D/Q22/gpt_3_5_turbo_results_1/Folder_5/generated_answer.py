
def find_sum_of_multiples(integer):
    multiples = [integer * i for i in range(1, 14)]
    return sum(multiples)
