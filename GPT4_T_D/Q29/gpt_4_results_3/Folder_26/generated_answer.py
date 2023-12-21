
def gcf_two_nums(nums_list):
    def compute_gcf(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    return compute_gcf(nums_list[49], nums_list[31])
