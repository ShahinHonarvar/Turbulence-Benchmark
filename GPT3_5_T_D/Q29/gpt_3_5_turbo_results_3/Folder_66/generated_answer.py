
def gcf_two_nums(lst):
    def find_gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    return find_gcf(lst[86], lst[89])
