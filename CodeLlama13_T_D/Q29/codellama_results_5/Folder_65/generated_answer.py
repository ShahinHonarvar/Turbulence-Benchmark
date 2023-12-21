
def gcf_two_nums(numbers):
    return get_gcd(numbers[29], numbers[53])

def get_gcd(a, b):
    if a == 0:
        return b
    return get_gcd(b % a, a)
