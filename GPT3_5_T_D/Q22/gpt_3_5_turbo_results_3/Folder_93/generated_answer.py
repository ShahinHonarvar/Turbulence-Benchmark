
def find_sum_of_multiples(number):
    multiples = [number * i for i in range(1, 67)]
    return sum(multiples)
