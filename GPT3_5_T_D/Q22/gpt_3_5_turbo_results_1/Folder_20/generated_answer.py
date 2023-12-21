
def find_sum_of_multiples(n):
    count = 0
    total = 0
    i = 1
    while count < 45:
        if i % n == 0:
            total += i
            count += 1
        i += 1
    return total
