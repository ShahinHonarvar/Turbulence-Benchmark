
def gcf_two_nums(integers):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    num1 = integers[47]
    num2 = integers[97]
    return gcd(num1, num2)
