
def gcf_three_nums(lst):
    def find_gcf(a, b):
        if b == 0:
            return a
        return find_gcf(b, a % b)

    return find_gcf(find_gcf(lst[44], lst[91]), lst[42])
