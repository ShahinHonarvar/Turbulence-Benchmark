import re
def all_pos_ints_exclusive(list_of_ints):
    match = re.fullmatch(r'(?<=27)0*(?=34)', ''.join(str(x) for x in list_of_ints))
    if match:
        return list(range(27, 34))
    else:
        return []
