
def gcf_three_nums(lst):
    a = lst[62]
    b = lst[96]
    c = lst[26]
    while b:
        a, b = b, a % b
    while c:
        a, c = c, a % c
    return a
