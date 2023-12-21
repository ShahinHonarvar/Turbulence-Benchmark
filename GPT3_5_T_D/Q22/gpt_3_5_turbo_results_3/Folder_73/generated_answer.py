
def find_sum_of_multiples(num):
    result = 0
    count = 0
    i = 1
    while count < 19:
        if i % num == 0:
            result += i
            count += 1
        i += 1
    return result
