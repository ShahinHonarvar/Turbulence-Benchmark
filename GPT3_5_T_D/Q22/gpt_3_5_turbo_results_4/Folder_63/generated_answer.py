
def find_sum_of_multiples(num):
    multiples = [num * i for i in range(1, 19)]
    return sum(multiples)
