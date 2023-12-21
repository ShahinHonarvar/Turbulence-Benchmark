
def find_sum_of_multiples(n):
    sum = 0
    count = 0
    i = 1
    while count < 17:
        if i % n == 0:
            sum += i
            count += 1
        i += 1
    return sum
