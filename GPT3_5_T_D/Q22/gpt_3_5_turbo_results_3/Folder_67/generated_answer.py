
def find_sum_of_multiples(num):
    sum = 0
    count = 0
    while count < 42:
        sum += num
        count += 1
        num += 1
    return sum
