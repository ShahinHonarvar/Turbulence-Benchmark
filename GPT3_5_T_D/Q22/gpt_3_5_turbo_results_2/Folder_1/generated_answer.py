
def find_sum_of_multiples(n):
    multiples_sum = 0
    count = 0

    while count < 51:
        multiples_sum += n
        count += 1
        n += n

    return multiples_sum
