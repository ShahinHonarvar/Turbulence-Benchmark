
def find_sum_of_multiples(n):
    multiples_sum = 0
    count = 0
    current = n
    
    while count < 57:
        multiples_sum += current
        current += n
        count += 1
        
    return multiples_sum
