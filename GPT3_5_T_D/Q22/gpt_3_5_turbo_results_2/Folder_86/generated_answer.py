
def find_sum_of_multiples(num):
    total = 0
    count = 0
    
    while count < 181:
        total += num
        count += 1
        num += 1
    
    return total
