
def find_sum_of_multiple(n):
    sum_of_multiple = 0
    for i in range(1, 89):
        sum_of_multiple += n*i
    return sum_of_multiple
