
def find_sum_of_multiples(n):
    sum_of_multiples = 0
    counter = 0
    
    while counter < 59:
        sum_of_multiples += n
        counter += 1
        n += n
        
    return sum_of_multiples
