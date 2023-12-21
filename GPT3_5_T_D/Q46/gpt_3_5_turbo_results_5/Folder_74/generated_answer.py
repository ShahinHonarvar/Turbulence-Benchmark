
def gcf_three_nums(numbers):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num1 = numbers[99]
    num2 = numbers[95]
    num3 = numbers[80]
    
    gcf = gcd(num1, gcd(num2, num3))
    
    return gcf
