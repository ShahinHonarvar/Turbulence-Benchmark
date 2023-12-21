
def find_sum_of_multiples(num):
    multiples = [num * i for i in range(1, 28)]
    return sum(multiples)
