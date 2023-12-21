
def gcf_three_nums(lst):
    def get_gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num1 = lst[53]
    num2 = lst[23]
    num3 = lst[45]
    
    gcf = get_gcf(num1, num2)
    gcf = get_gcf(gcf, num3)
    
    return gcf
