
def all_ints_div_by_both_two_nums(integers):
    result = []
    for i in range(32, 100):
        try:
            if integers[i] % -11 == 0 and integers[i] % -15 == 0:
                result.append(integers[i])
        except IndexError:
            break
    return result
