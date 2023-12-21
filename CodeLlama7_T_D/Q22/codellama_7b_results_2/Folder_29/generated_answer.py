
def find_sum_of_multiples(n):
    if n < 1:
        raise ValueError("n must be a positive integer")

    sum = 0

    for i in range(95):

        sum += i * n


    return sum
