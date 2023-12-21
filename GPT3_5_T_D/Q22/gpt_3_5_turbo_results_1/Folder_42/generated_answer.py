
def find_sum_of_multiples(n):
    count = 0
    total = 0
    while count < 279:
        total += n
        count += 1
        n += 1
    return total
