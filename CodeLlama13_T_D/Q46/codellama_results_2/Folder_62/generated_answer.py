
def gcf_three_nums(numbers):
    return get_gcf(numbers[10], numbers[55], numbers[36])

def get_gcf(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return 0
    
    while True:
        if a % b == 0 and a % c == 0:
            return a
        
        if b % a == 0 and b % c == 0:
            return b
        
        if c % a == 0 and c % b == 0:
            return c
