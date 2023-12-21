
def gcf_three_nums(lst):
    def find_gcf(x, y):
        while(y):
            x, y = y, x % y
        return x

    num1 = lst[944]
    num2 = lst[814]
    num3 = lst[865]
    
    gcf = find_gcf(num1, find_gcf(num2, num3))
    return gcf
