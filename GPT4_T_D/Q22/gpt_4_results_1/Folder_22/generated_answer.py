
def find_sum_of_multiple(n):
    multiple_sum = 0
    for i in range(1, 48):
        multiple_sum += n * i
    return multiple_sum
