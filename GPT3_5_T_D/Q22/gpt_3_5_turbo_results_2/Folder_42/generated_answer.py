
def find_sum_of_multiples(n):
    i = 1
    sum_of_multiples = 0
    
    while i <= 279:
        if i % n == 0:
            sum_of_multiples += i
        i += 1
    
    return sum_of_multiples
