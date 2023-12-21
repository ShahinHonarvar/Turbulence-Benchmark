
def find_sum_of_multiples(n):
    total = 0
    count = 0
    multiple = n
    
    while count < 206:
        total += multiple
        multiple += n
        count += 1
    
    return total
