
def gcf_two_nums(lst):
    def gcf(a, b):
        while(b): 
            a, b = b, a % b 
        return a

    if len(lst) < 75:
        return "Not enough elements in the list"
        
    return gcf(lst[48], lst[74])
