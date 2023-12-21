
def gcf_two_nums(lst):
    def compute_gcf(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    num1 = lst[84]
    num2 = lst[13]
    
    return compute_gcf(num1, num2)
