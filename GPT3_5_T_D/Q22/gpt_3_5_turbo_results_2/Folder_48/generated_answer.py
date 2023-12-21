
def find_sum_of_multiples(n):
    sum = 0
    count = 0
    i = 1
    while count < 186:
        multiple = n * i
        sum += multiple
        count += 1
        i += 1
    return sum
