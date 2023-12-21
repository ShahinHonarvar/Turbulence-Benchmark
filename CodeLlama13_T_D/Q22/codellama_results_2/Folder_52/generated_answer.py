
def find_sum_of_multiples(n):
    sum = 0
    for i in range(1, 423):
        if n * i <= 0:
            break
        sum += n * i
    return sum
