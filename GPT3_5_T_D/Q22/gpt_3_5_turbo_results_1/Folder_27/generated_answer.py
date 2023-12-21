
def find_sum_of_multiples(n):
    multiples = []
    count = 0
    
    for i in range(1, 10000):
        if i % n == 0:
            multiples.append(i)
            count += 1
        
        if count == 54:
            break
    
    return sum(multiples)
