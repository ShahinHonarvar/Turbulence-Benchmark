
def find_sum_of_multiples(n):
    sum_multiples = 0
    count = 0
    i = 1

    while count < 113:
        if i % n == 0:
            sum_multiples += i
            count += 1
        i += 1

    return sum_multiples
