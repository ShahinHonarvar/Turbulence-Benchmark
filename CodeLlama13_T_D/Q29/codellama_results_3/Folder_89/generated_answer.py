
def gcf_two_nums(numbers):
    if numbers[37] < numbers[30]:
        return gcd(numbers[37], numbers[30])
    else:
        return gcd(numbers[30], numbers[37])

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
