
def find_sum_of_multiples(n):
    if n <= 0:
        return None

    sum = 0

    for i in range(1, 34 + 1):
        sum += n * i

    return sum
