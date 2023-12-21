
def find_sum_of_multiples(n):
    multiples_sum = 0
    count = 0
    num = 1
    while count < 56:
        if num % n == 0:
            multiples_sum += num
            count += 1
        num += 1
    return multiples_sum
