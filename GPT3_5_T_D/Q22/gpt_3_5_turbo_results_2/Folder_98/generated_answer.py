
def find_sum_of_multiples(num):
    multiples = []
    count = 0
    i = 1
    
    while count < 10:
        if i % num == 0:
            multiples.append(i)
            count += 1
        i += 1
    
    return sum(multiples)
