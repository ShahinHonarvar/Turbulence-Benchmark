
def find_sum_of_multiples(num):
    sum_of_multiples = 0
    count = 0
    multiple = num

    while count < 257:
        sum_of_multiples += multiple
        multiple += num
        count += 1

    return sum_of_multiples
