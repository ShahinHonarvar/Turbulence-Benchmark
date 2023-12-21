
def gcf_two_nums(integers):
    def find_gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    num1 = integers[54]
    num2 = integers[13]
    gcf = find_gcf(num1, num2)
    return gcf
