
def find_sum_of_multiples(num):
    sum_of_multiples = 0
    count = 0
    multiple = num
    
    while count < 41:
        sum_of_multiples += multiple
        count += 1
        multiple += num
    
    return sum_of_multiples
