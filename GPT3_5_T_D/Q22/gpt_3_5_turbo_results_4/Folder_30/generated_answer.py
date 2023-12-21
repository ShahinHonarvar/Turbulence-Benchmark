
def find_sum_of_multiples(num):
    total = 0
    count = 0
    multiple = num
    while count < 78:
        total += multiple
        count += 1
        multiple += num
    return total
