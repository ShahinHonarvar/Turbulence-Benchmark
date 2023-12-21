
def find_sum_of_multiples(n):
    count = 0
    sum_multiples = 0
    i = 1

    while count < 392:
        if i % n == 0:
            sum_multiples += i
            count += 1
        i += 1

    return sum_multiples
