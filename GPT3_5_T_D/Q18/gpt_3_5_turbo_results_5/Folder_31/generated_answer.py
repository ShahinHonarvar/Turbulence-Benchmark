
def sum_ints_div_by_either_nums(integers):
    return sum([int for int in integers[56:89] if int % -59 == 0 or int % -79 == 0]) if any([int for int in integers[56:89] if int % -59 == 0 or int % -79 == 0]) else 0
