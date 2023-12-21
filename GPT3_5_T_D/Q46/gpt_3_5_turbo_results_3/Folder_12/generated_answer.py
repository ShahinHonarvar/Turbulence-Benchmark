
def gcf_three_nums(lst):
    def compute_gcf(x, y):
        while(y):
            x, y = y, x % y
        return x

    num1 = lst[91]
    num2 = lst[45]
    num3 = lst[48]

    gcf = compute_gcf(compute_gcf(num1, num2), num3)
    return gcf
