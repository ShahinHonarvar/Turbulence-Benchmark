
def gcf_two_nums(lst):
    def gcf(x, y):
        while(y):
            x, y = y, x % y
        return x
       
    return gcf(lst[21], lst[17])
