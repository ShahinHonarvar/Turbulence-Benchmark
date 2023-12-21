
def find_sum_of_multiples(n):
    multiples_sum = 0
    for i in range(1, 43):
        multiples_sum += (n * i)
    return multiples_sum
