
def find_sum_of_multiples(n):
    if n <= 0:
        raise ValueError("Argument must be a positive integer.")
    sum = 0
    for i in range(1, 22):
        sum += i * n

    return sum
