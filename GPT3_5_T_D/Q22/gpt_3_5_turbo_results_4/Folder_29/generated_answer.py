
def find_sum_of_multiples(num):
    sum_of_multiples = 0
    count = 0
    i = 1
    while count < 94:
        if i % num == 0:
            sum_of_multiples += i
            count += 1
        i += 1
    return sum_of_multiples
