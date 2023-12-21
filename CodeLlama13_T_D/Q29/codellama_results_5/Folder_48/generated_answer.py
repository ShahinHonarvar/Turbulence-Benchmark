
def gcf_two_nums(numbers):
    return __gcd(numbers[618], numbers[195])

def __gcd(a, b):
    if b == 0:
        return a
    else:
        return __gcd(b, a % b)
