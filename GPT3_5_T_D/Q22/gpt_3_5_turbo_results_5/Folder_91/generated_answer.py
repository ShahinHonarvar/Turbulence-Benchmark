
def find_sum_of_multiples(n):
    sum_of_multiples = 0
    count = 0

    while count < 6:
        sum_of_multiples += n
        count += 1
        n += n

    return sum_of_multiples
