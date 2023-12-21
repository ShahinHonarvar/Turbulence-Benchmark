
def find_sum_of_multiples(n):
    sum = 0
    count = 0
    multiple = n
    
    while count < 40:
        sum += multiple
        multiple += n
        count += 1
    
    return sum
