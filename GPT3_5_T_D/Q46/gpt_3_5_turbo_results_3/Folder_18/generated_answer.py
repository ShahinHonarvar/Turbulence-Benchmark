
def gcf_three_nums(lst):
    def find_gcf(x, y):
        while y:
            x, y = y, x % y
        return x

    a = lst[637]
    b = lst[411]
    c = lst[757]

    gcf_ab = find_gcf(a, b)
    gcf_abc = find_gcf(gcf_ab, c)

    return gcf_abc
