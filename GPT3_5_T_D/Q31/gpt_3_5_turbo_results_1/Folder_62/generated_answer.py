
def if_perfect_num(lst):
    num = lst[926]
    if sum([x for x in range(1, num) if num % x == 0]) == num:
        return True
    else:
        return False
