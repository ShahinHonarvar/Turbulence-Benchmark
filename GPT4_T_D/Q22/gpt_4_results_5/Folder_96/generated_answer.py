
def find_sum_of_multiples(n):
    sum = 0
    for i in range(1, 98):
        sum += i * n
    return sum
