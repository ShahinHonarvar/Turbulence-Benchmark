
def find_sum_of_multiples(number):
    multiples_sum = 0
    for i in range(1, 280):
        multiples_sum += number * i
    return multiples_sum
