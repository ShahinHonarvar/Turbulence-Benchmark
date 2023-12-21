
def gcf_two_nums(integers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num_1 = integers[24]
    num_2 = integers[68]
    gcf = gcd(num_1, num_2)
    return gcf
