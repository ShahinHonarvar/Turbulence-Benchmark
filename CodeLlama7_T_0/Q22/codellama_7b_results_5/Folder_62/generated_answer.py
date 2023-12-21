
def find_sum_of_multiples(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")

    sum = 0

    for i in range(1, 189):

        if i % n == 0:

            sum += i


    return sum
