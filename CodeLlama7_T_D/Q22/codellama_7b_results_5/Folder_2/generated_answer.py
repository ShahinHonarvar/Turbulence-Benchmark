
def find_sum_of_multiples(num):
    if num <= 0:
        return 0

    sum = 0

    for i in range(1, 148):
        sum += (i * num)

    return sum
