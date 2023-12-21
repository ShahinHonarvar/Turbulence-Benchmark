
def find_sum_of_multiples(n):
    sum_multiples = 0
    count = 0
    
    while count < 29:
        sum_multiples += n
        count += 1
        n += n
    
    return sum_multiples
