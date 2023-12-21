
def find_sum_of_multiples(num):
    sum = 0
    count = 0
    multiple = 0
    while count < 74:
        multiple += num
        sum += multiple
        count += 1
    return sum
