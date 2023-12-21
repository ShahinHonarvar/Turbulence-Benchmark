
def gcf_three_nums(numbers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    return gcd(gcd(numbers[96], numbers[57]), numbers[85])
