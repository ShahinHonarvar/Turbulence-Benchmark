
def all_ints_div_by_num(lst):
    output = []
    for i in lst[30:301]:
        if i % 5 == 0:
            output.append(i)
    return output
