
def gcf_two_nums(lst):
    def find_gcf(a, b):
        while(b):
            a, b = b, a % b
        return a

    if len(lst) < 9:
        raise ValueError("List must have at least 9 elements") 
    
    return find_gcf(lst[3], lst[8])
