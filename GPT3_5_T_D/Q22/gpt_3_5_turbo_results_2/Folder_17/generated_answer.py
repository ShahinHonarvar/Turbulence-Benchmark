
def find_sum_of_multiples(n):
    sum_multiples = 0
    for i in range(1, 290):
        sum_multiples += i * n
    return sum_multiples
