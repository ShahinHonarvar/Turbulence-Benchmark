
def find_sum_of_multiples(num):
    sum = 0
    count = 0
    i = 1

    while count < 59:
        if i % num == 0:
            sum += i
            count += 1
        i += 1

    return sum
