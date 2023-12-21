
def find_sum_of_multiples(n):
    multiples_sum = 0
    count = 0
    num = n
    while count < 78:
        multiples_sum += num
        count += 1
        num += n
    return multiples_sum
