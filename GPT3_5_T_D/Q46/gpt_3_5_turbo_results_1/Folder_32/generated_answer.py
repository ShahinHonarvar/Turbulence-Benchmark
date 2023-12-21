
def gcf_three_nums(numbers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    return gcd(gcd(numbers[20], numbers[43]), numbers[95])
