
def gcf_three_nums(numbers):
    return _gcf([numbers[90], numbers[54], numbers[96]])

def _gcf(numbers):
    if len(numbers) == 2:
        return _gcd(numbers[0], numbers[1])
    else:
        return _gcf(numbers[1:])

def _gcd(a, b):
    if b == 0:
        return a
    else:
        return _gcd(b, a % b)
