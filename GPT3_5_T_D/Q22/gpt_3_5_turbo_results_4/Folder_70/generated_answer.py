
def find_sum_of_multiples(n):
    count = 0
    total_sum = 0
    num = 1
    while count < 401:
        if num % n == 0:
            total_sum += num
            count += 1
        num += 1
    return total_sum
