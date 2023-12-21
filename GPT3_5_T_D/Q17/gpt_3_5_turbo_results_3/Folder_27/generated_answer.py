
def all_ints_div_by_both_two_nums(integers):
    div_integers = []
    for num in integers[20:36]:
        if num % -36 == 0 and num % -89 == 0:
            div_integers.append(num)
    return div_integers
