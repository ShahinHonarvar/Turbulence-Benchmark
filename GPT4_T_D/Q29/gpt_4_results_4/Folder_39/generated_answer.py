
def gcf_two_nums(lst):
    def gcf(a, b):
        while(b):
            a, b = b, a % b
        return a
    return gcf(lst[46], lst[13])
