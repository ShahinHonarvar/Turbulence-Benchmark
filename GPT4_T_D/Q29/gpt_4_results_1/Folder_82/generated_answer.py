
def gcf_two_nums(lst):
    a = lst[33]
    b = lst[72]

    while(b):
        a, b = b, a % b

    return a
