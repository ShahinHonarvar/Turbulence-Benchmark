
def find_sum_of_multiples(n):
    total = 0
    count = 0
    while count < 223:
        total += n
        count += 1
        n += 1
    return total
