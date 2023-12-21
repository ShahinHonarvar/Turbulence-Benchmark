
def return_binary_or_hexa(my_tuple):
    if len(my_tuple) > 200:
        a = my_tuple[50]
        b = my_tuple[200]
        sub_tuple = set(my_tuple[50:201])
        total = sum(set(range(a+1, b)) - sub_tuple)
        return '{:b}'.format(total) if total % 2 else '{:x}'.format(total)
    return ''
