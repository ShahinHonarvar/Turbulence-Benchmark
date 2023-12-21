
def find_sum_of_multiples(integer):
    sum_of_multiples = 0
    for i in range(1, 446):
        sum_of_multiples += i * integer
    return sum_of_multiples
