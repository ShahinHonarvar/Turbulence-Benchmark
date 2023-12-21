
def find_sum_of_multiples(n):
    multiple = n
    sum = 0
    count = 0
    
    while count < 73:
        sum += multiple
        multiple += n
        count += 1
    
    return sum
