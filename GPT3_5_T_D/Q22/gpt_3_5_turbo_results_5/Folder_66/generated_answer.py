
def find_sum_of_multiples(num):
    total = 0
    count = 0
    i = 1
    
    while count < 25:
        if i % num == 0:
            total += i
            count += 1
        i += 1
    
    return total
