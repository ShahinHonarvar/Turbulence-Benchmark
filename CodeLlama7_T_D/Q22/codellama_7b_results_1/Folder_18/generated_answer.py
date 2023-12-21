
def find_sum_of_multiples(num):
    sum = 0
    for i in range(1, 392 + 1):
        if i % num == 0:
            sum += i

    return sum
