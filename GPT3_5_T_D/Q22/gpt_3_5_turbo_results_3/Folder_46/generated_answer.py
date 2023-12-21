
def find_sum_of_multiples(number):
    sum_of_multiples = 0
    count = 0
    current_number = 0
    
    while count < 464:
        current_number += number
        sum_of_multiples += current_number
        count += 1
    
    return sum_of_multiples
