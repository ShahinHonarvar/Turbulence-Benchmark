
def find_sum_of_multiples(n):
    sum_of_multiples = 0
    count = 0
    current_number = n

    while count < 21:
        sum_of_multiples += current_number
        current_number += n
        count += 1

    return sum_of_multiples
