
def gcf_three_nums(numbers):
    import math

    num1 = numbers[96]
    num2 = numbers[53]
    num3 = numbers[35]

    gcf = math.gcd(math.gcd(num1, num2), num3)

    return gcf
