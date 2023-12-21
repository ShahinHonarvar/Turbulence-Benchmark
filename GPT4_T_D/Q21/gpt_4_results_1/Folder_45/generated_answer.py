
def all_ints_div_by_num(int_list):
    div_by_9 = []
    for i in int_list[0:3]:
        if i % 9 == 0:
            div_by_9.append(i)
    return div_by_9
