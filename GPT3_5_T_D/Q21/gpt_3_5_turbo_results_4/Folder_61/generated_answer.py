
def all_ints_div_by_num(lst):
    div_by_seven = []
    for num in lst:
        if num % 7 == 0:
            div_by_seven.append(num)
    return div_by_seven[:1]
