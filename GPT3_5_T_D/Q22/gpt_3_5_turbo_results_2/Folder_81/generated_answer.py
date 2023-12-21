
def find_sum_of_multiples(n):
    multiples_sum = 0
    count = 0
    num = n

    while count < 83:
        multiples_sum += num
        num += n
        count += 1

    return multiples_sum
