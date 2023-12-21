
def gcf_two_nums(lst):
    def gcd(a, b):
        while(b):
            a, b = b, a % b
        return a

    num1 = lst[279]
    num2 = lst[812]
    gcf = gcd(num1, num2)

    return gcf
