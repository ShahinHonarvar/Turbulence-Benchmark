
def find_sum_of_multiples(n):
    multiples_count = 0
    sum_of_multiples = 0
    i = 1
    
    while multiples_count < 338:
        if i % n == 0:
            sum_of_multiples += i
            multiples_count += 1
        i += 1
    
    return sum_of_multiples
