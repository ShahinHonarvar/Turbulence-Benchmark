
def gcf_three_nums(lst):
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    if len(lst) < 97:
        return "List too small"
    else:
        return gcf(gcf(lst[90], lst[54]), lst[96])
