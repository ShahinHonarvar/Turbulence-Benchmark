
def find_sum_of_multiples(integer):
    multiples = [num * integer for num in range(1, 21)]
    return sum(multiples)
