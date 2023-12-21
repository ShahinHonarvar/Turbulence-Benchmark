
def find_sum_of_multiples(n):
    sum_of_multiples = 0
    for i in range(1, 256):
        sum_of_multiples += n * i
    return sum_of_multiples
