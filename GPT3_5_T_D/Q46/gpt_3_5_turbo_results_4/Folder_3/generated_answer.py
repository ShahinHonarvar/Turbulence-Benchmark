
def gcf_three_nums(lst):
    def find_gcf(a, b):
        while b:
            a, b = b, a % b
        return a

    a = lst[31]
    b = lst[69]
    c = lst[40]

    gcf_a_b = find_gcf(a, b)
    gcf = find_gcf(gcf_a_b, c)

    return gcf
