
def find_sum_of_multiples(n):
    if n <= 0:
        raise ValueError("The input must be a positive integer.")
    sum = 0
    for i in range(1, 318 + 1):
        if i % n == 0:
            sum += i

    return sum
