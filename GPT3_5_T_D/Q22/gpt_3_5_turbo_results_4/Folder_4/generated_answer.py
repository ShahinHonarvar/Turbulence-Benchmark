
def find_sum_of_multiples(n):
    total = 0
    count = 0
    num = n
    while count < 40:
        total += num
        count += 1
        num += n
    return total
