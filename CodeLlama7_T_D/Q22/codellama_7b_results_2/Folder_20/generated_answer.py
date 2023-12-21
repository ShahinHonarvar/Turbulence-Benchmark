
def find_sum_of_multiples(num):
    sum = 0
    for i in range(1, 46):
        sum += num * i

    return sum
