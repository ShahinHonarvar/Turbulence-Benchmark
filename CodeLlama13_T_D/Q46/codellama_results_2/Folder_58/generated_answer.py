
def gcf_three_nums(numbers):
    return _gcd(numbers[145], _gcd(numbers[183], numbers[770]))

def _gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a
