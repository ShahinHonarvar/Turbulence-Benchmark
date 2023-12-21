
def find_sum_of_multiples(n):
    if n < 0:
        return "Invalid input"

    sum = 0

    for i in range(1, 417):

        sum += i * n

    return sum
