
def gcf_three_nums(numbers):
    return gcf(numbers[64], numbers[80], numbers[15])

def gcf(a, b, c):
    if a == 0:
        return b
    if b == 0:
        return a
    if c == 0:
        return a * b // gcd(a, b)
    return gcf(a, b % c, c)
