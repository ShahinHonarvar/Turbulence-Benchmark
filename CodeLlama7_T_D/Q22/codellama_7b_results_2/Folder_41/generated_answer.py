
def find_sum_of_multiples(num):
    if num < 1:
        return 0

    sum = 0

    for i in range(1, 64):
        sum += i * num

    return sum
