
def gcf_three_nums(numbers):
    x = numbers[34]
    y = numbers[38]
    z = numbers[77]
    
    while y:
        x, y = y, x % y
        
    while z:
        x, z = z, x % z
        
    return x
