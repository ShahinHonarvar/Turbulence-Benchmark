
def find_sum_of_multiples(n):
    sum = 0
    for i in range(1, n*57+1, n):
        sum += i
    return sum
