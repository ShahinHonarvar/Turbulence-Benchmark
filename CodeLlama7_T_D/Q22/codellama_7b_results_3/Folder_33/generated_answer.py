
def find_sum_of_multiples(num):
    if num <= 0:
        raise ValueError("The input number must be positive")

    sum = 0

    for i in range(1, 476):

        sum += num * i


    return sum
