
def sum_odd_ints_inclusive(my_list):
    return sum(int for i, int in enumerate(my_list) if i >= 310 and i <= 370 and int % 2 != 0)
