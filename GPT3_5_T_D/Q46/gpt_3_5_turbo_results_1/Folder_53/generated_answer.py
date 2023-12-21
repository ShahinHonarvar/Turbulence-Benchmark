
def gcf_three_nums(numbers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    return gcd(gcd(numbers[66], numbers[56]), numbers[92])
