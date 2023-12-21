
def find_sum_of_multiples(n):
    sum_of_multiples = 0
    count = 1
    while count <= 279:
        sum_of_multiples += (count * n)
        count += 1
    return sum_of_multiples
