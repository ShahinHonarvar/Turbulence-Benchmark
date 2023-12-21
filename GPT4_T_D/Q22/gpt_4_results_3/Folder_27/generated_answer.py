
def find_sum_of_multiples(n):
    total_sum = 0
    for i in range(1, 55):
        total_sum += i * n
    return total_sum
