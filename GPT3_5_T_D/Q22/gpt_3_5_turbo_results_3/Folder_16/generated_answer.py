
def find_sum_of_multiples(num):
    sum = 0
    count = 0
    
    while count < 255:
        if num % 2 == 0:
            sum += num
            count += 1
        num += 1
    
    return sum
