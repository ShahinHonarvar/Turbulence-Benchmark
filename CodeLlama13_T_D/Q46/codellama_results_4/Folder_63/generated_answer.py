
def gcf_three_nums(numbers):
    indices = [38, 52, 69]
    return _gcd(numbers[indices[0]], _gcd(numbers[indices[1]], numbers[indices[-1]]))

def _gcd(a, b):
    if b == 0:
        return a
    else:
        return _gcd(b, a % b)
