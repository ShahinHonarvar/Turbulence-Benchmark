
def find_sum_of_multiples(n):
    sum_multiples = 0
    for i in range(1, 339):
        sum_multiples += n*i
    return sum_multiples
