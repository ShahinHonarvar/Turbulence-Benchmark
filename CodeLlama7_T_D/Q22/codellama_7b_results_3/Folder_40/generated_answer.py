
def find_sum_of_multiples(n):
    if n < 1:
        return 0

    sum = 0

    for i in range(1, n + 1):
        if i % n == 0:
            sum += i

    return sum
