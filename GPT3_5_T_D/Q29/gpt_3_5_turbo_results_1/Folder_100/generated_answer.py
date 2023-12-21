
def gcf_two_nums(lst):
    def get_gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    return get_gcf(lst[96], lst[32])
