
def find_sum_of_multiples(num):
    sum_of_multiples = 0
    counter = 0
    
    for i in range(1, 1000000):
        if i % num == 0:
            sum_of_multiples += i
            counter += 1
            
            if counter == 173:
                break
    
    return sum_of_multiples
