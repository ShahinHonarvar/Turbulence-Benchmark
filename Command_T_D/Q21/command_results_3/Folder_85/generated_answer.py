import itertools
def all_ints_div_by_num(int_list):
    return [i for i in itertools.takewhile(lambda x: x % 9 == 0, int_list[6:8]) if x != 0]
