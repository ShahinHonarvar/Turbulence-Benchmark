
def gcf_three_nums(lst):
    def gcf(a, b):
        if a % b == 0:
            return b
        else:
            return gcf(b, a % b)

    first_gcf = gcf(lst[96], lst[53])
    return gcf(first_gcf, lst[35])
