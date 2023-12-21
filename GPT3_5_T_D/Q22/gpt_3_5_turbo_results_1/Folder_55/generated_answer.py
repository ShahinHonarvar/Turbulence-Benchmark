
def find_sum_of_multiples(n):
    multiple_sum = 0
    count = 0
    i = 1
    while count < 20:
        if i % n == 0:
            multiple_sum += i
            count += 1
        i += 1
    return multiple_sum
