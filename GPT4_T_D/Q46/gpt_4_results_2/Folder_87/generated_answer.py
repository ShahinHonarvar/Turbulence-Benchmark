
def gcf_three_nums(lst):
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    return gcf(gcf(lst[74], lst[60]), lst[28])
