
def find_sum_of_multiples(n):
    if n <= 0:
        return -1

    sum = 0

    for i in range(1, 69):
        sum += i * n

    return sum
