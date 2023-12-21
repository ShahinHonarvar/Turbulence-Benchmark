
def find_sum_of_multiples(n):
    total = 0
    count = 0
    i = 1
    while count < 9:
        if i % n == 0:
            total += i
            count += 1
        i += 1
    return total
