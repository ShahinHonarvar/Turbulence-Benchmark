 
def find_sum_of_multiples(number):
    sum = 0
    count = 0
    
    while count < 95:
        sum += number
        number += number
        count += 1
    
    return sum
