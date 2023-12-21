
def find_sum_of_multiples(n):
    total = 0
    counter = 0
    while counter < 289:
        total += n
        counter += 1
        n += 1
    return total
