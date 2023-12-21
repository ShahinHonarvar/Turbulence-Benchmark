
def gcf_three_nums(lst):
    def find_gcf(a, b):
        while b:
            a, b = b, a % b
        return a

    return find_gcf(find_gcf(lst[145], lst[183]), lst[770])
