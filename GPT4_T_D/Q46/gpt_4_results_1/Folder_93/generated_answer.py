
def gcf_three_nums(lst):
    def gcf(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    x = lst[25]
    y = lst[76]
    z = lst[57]

    result = gcf(gcf(x, y), z)

    return result
