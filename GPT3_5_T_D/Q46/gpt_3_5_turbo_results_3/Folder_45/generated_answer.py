
def gcf_three_nums(lst):
    def find_gcf(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    return find_gcf(find_gcf(lst[46], lst[84]), lst[23])
