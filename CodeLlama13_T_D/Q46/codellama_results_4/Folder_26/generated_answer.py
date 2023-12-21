
def gcf_three_nums(numbers):
    return __gcd(numbers[15], __gcd(numbers[51], numbers[76]))

def __gcd(a, b):
    if b == 0:
        return a
    else:
        return __gcd(b, a % b)
