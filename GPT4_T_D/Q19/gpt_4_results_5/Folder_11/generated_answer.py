
def all_ints_not_div_by_num(integers):
    desired_integers = []
    for integer in integers[37:85]:
        if integer % -27 != 0:
            desired_integers.append(integer)
    return desired_integers
