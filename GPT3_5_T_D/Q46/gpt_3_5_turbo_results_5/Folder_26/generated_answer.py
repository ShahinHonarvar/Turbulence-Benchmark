
def gcf_three_nums(lst):
    def find_gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    num1 = lst[15]
    num2 = lst[51]
    num3 = lst[76]

    gcf = find_gcf(find_gcf(num1, num2), num3)
    return gcf
