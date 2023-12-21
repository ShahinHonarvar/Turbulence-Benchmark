
def gcf_three_nums(lst):
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    return gcf(gcf(lst[96], lst[57]), lst[85])
