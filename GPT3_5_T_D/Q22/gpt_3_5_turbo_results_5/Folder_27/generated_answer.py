
def find_sum_of_multiples(n):
    sum = 0
    count = 0
    
    for i in range(1, n+1):
        if count == 54:
            break
        if i % n == 0:
            sum += i
            count += 1
    
    return sum
