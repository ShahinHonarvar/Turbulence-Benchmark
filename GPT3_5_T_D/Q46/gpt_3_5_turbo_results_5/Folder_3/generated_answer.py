
def gcf_three_nums(numbers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    a = numbers[31]
    b = numbers[69]
    c = numbers[40]
    
    gcd_ab = gcd(a, b)
    gcd_abc = gcd(gcd_ab, c)
    
    return gcd_abc
