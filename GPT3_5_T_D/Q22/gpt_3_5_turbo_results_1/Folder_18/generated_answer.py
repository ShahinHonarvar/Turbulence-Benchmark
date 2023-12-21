
def find_sum_of_multiples(num):
    sum = 0
    count = 0
    multiple = num

    while count < 392:
        sum += multiple
        count += 1
        multiple += num

    return sum
