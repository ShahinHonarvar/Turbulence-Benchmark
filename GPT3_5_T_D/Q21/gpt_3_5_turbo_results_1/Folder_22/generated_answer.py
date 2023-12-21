
def all_ints_div_by_num(integers):
    div_by_num = []
    for i in range(10, 11):
        if integers[i] % 1 == 0:
            div_by_num.append(integers[i])
    return div_by_num
