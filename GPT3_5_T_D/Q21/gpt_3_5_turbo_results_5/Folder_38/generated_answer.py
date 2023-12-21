
def all_ints_div_by_num(integers):
    div_ints = []
    for i in range(12, 16):
        if integers[i] % -80 == 0:
            div_ints.append(integers[i])
    return div_ints
