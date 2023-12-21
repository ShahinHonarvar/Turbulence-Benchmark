
def find_sum_of_multiple(n):
    sum_of_multiples = 0
    for i in range(1, 446):
        sum_of_multiples += n * i
    return sum_of_multiples
