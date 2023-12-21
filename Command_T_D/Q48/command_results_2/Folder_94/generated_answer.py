
def return_binary_or_hexa(lst):
    lst = sorted(set(lst))
    a = lst[42] + 1
    b = lst[87] - 1
    lst = lst[a:b + 1]
    lst = [n for n in range(a, b + 1) if n not in lst]
    if len(lst) % 2 == 1:
        return format(sum(lst), 'b')
    else:
        return format(sum(lst), 'x')
