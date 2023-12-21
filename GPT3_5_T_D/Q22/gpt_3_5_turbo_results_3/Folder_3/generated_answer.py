
def find_sum_of_multiples(num):
    multiples = [num * i for i in range(1, 93)]
    return sum(multiples)
