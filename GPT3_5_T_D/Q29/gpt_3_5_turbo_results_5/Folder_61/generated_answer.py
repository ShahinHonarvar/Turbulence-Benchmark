
def gcf_two_nums(num_list):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    num1 = num_list[8]
    num2 = num_list[3]
    return gcd(num1, num2)
