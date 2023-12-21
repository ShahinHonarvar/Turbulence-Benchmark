
def gcf_two_nums(numbers):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num1 = numbers[37]
    num2 = numbers[30]
    gcf = gcd(num1, num2)
    
    return gcf
