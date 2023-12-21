
def gcf_three_nums(lst):
    def find_gcf(a, b):
        while(b):
            a, b = b, a % b
        return a

    a = lst[8]
    b = lst[9]
    c = lst[3]

    gcf = find_gcf(a, b)
    gcf = find_gcf(gcf, c)

    return gcf
