
def find_sum_of_multiples(n):
    multiples = []
    num = 1
    
    while len(multiples) < 475:
        if num % n == 0:
            multiples.append(num)
        num += 1
    
    return sum(multiples)
