
def find_sum_of_multiples(n):
    if n < 1:
        raise ValueError("The input must be a positive integer.")
    sum = 0
    for i in range(1, 223):
        sum += i * n
    return sum
