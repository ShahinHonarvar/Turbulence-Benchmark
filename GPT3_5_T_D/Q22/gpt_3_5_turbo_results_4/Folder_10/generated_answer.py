
def find_sum_of_multiples(n):
    total = 0
    count = 0
    mul = n
    
    while count < 100:
        total += mul
        count += 1
        mul += n
    
    return total
