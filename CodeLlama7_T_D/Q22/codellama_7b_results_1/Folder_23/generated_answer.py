
def find_sum_of_multiples(n):
    sum = 0
    for i in range(1, 42):
        if i % n == 0:
            sum += i

    return sum
