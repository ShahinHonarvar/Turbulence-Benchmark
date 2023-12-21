
def find_sum_of_multiples(integer):
    sum_of_multiples = 0
    count = 0
    number = 1
    while count < 4:
        if number % integer == 0:
            sum_of_multiples += number
            count += 1
        number += 1
    return sum_of_multiples
