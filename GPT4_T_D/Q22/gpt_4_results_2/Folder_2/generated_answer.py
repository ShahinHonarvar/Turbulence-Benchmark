
def find_sum_of_multiples(n):
    sum_of_multiples = 0
    for i in range(1, 148):
        sum_of_multiples += i * n
    return sum_of_multiples
