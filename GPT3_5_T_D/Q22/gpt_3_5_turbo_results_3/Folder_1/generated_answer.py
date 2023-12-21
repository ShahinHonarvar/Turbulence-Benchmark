
def find_sum_of_multiples(num):
    sum_of_multiples = 0
    for i in range(1, 52):
        sum_of_multiples += num * i
    return sum_of_multiples
