
def gcf_two_nums(lst):
    def find_gcf(a, b):
        while b:
            a, b = b, a % b
        return a
    
    return find_gcf(lst[360], lst[722])
