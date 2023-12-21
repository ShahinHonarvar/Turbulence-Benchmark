
def gcf_two_nums(numbers):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    return gcd(numbers[6], numbers[9])
