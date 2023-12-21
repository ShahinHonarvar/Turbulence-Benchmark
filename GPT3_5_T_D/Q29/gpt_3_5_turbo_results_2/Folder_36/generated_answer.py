
def gcf_two_nums(numbers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    return gcd(numbers[429], numbers[289])
