
def find_sum_of_multiples(num):
    sum_of_multiples = 0
    count = 1
    while count <= 116:
        sum_of_multiples += (num * count)
        count += 1
    return sum_of_multiples
