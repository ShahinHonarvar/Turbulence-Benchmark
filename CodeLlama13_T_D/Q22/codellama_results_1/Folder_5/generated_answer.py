
def find_sum_of_multiples(n):
    sum = 0
    for i in range(1, 13):
        sum += n * i
    return sum
