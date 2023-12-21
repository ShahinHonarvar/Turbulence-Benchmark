
def gcf_three_nums(lst):
    def find_gcf(a, b):
        while b:
            a, b = b, a % b
        return a
    
    return find_gcf(find_gcf(lst[64], lst[80]), lst[15])
