
def gcf_three_nums(numbers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    return gcd(numbers[40], gcd(numbers[15], numbers[99]))
