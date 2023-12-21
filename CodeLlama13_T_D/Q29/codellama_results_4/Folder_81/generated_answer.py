
def gcf_two_nums(numbers):
    return _gcd(numbers[20], numbers[83])

def _gcd(a, b):
    if a == 0:
        return b
    else:
        return _gcd(b % a, a)
