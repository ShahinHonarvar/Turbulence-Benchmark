
def find_sum_of_multiples(num):
    sum_of_multiples = 0
    count = 1
    
    while count <= 186:
        multiple = num * count
        sum_of_multiples += multiple
        count += 1
    
    return sum_of_multiples
