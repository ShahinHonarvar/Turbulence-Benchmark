
def find_sum_of_multiples(n):
    if n < 1:
        return None

    sum = 0

    for i in range(1, 81):
        sum += i * n

    return sum
