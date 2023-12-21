
def find_sum_of_multiples(n):
    sum_multiple = 0
    for i in range(1, 39):
        sum_multiple += n * i
    return sum_multiple
