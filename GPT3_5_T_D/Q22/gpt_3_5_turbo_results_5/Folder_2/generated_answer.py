
def find_sum_of_multiples(n):
    multiples_sum = 0
    count = 0
    for i in range(1, 148):
        multiples_sum += i * n
        count += 1
        if count == 147:
            break
    return multiples_sum
