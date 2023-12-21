
def find_sum_of_multiples(n):
    total = 0
    for i in range(1, 54):
        total += i * n
    return total
