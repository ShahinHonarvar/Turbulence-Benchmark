
def gcf_two_nums(numbers):
    n1 = numbers[84]
    n2 = numbers[13]
    
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    
    return n1
