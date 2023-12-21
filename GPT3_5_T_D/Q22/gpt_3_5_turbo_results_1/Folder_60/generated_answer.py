
def find_sum_of_multiples(n):
    total = 0
    count = 0
    num = 1
    while count < 35:
        if num % n == 0:
            total += num
            count += 1
        num += 1
    return total
