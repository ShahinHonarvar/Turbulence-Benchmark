
def find_sum_of_multiples(num):
    total = 0
    count = 0
    multiple = num
    
    while count < 68:
        total += multiple
        multiple += num
        count += 1
    
    return total
