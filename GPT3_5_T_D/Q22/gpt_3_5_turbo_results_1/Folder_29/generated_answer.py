
def find_sum_of_multiples(n):
    i = 1
    sum_of_multiples = 0
    while i <= 94:
        sum_of_multiples += n * i
        i += 1
    return sum_of_multiples
