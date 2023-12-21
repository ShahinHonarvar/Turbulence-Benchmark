def all_odd_ints_inclusive(int_list):
    return [x for x in range(len(int_list)) if int_list[x] % 2 == 1]
