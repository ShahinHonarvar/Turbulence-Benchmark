import re
def all_pos_ints_exclusive(int_list):
    s = str(list(range(2, len(int_list) + 1)))
    reg = re.compile(r'(?<=\d)[2-8]')
    return [i for i in range(2, len(int_list) + 1) if reg.match(str(i))]
