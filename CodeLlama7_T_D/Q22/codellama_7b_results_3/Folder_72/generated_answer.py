
def find_sum_of_multiples(n):
    if n < 1:
        return -1

    sum = 0

    for i in range(1, 88):
        sum += i * n

    return sum
