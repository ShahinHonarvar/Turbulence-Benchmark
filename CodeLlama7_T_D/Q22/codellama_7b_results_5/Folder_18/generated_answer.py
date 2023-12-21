
def find_sum_of_multiples(num):
    if num < 1:
        return "Invalid input"

    sum = 0

    for i in range(1, 393):

        if i % num == 0:

            sum += i


    return sum
