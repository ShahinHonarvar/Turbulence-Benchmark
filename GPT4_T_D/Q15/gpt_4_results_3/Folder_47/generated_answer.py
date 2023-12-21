
def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 76:
        return 0
    else:
        return sum(num for num in int_list[37:77] if num % 2 != 0)
