
def find_sum_of_multiples(n):
    sum_of_multiples = 0
    for i in range(1, 424):
        multiple = n * i
        sum_of_multiples += multiple
    return sum_of_multiples
