
def find_sum_of_multiples(num):
    if num < 1:
        raise ValueError("Number must be positive")

    sum = 0

    for i in range(91):

        sum += num * (i + 1)

    return sum
