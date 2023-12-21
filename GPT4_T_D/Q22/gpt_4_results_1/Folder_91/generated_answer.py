
def find_sum_of_multiples(n):
    multiple_sum = 0
    for i in range(1, 7):
        multiple_sum += n * i
    return multiple_sum
