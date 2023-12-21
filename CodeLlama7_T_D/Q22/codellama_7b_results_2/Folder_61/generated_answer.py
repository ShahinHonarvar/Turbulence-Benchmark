
def find_sum_of_multiples(num):
    if num < 0:
        raise ValueError("The input must be a positive integer")

    sum = 0

    for i in range(1, 6):

        sum += num * i


    return sum
