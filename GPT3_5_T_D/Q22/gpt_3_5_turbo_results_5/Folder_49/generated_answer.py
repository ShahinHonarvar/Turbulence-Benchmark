
def find_sum_of_multiples(n):
    result = 0
    count = 0
    i = 1
    
    while count < 95:
        if i % n == 0:
            result += i
            count += 1
        i += 1
    
    return result
