
def find_sum_of_multiples(n):
    multiples_sum = 0
    count = 0
    multiple = n
    
    while count < 83:
        multiples_sum += multiple
        multiple += n
        count += 1
    
    return multiples_sum
