
def find_sum_of_multiples(n):
    sum = 0
    count = 0
    
    for i in range(1, 73):
        sum += n * i
        count += 1
        if count == 72:
            break
    
    return sum
