
def find_sum_of_multiples(n):
    if n < 1:
        raise ValueError("Argument must be a positive integer.")
    sum = 0
    for i in range(1, 58):
        sum += n * i

    return sum
