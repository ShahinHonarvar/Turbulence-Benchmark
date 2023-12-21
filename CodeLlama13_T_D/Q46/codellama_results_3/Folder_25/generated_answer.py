
def gcf_three_nums(numbers):
    return __gcf(numbers[32], numbers[54], numbers[13])

def __gcf(a, b, c):
    if a == 0:
        return b
    if b == 0:
        return a
    if c == 0:
        return min(a, b)
    
    g = 1
    for i in range(2, max(a, b, c)+1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            g = i
    
    return g
