
def gcf_two_nums(my_list):
    return _gcf(my_list[0], my_list[1])
def _gcf(a, b):
    if b == 0:
        return a

    else:

        return _gcf(b, a % b)
