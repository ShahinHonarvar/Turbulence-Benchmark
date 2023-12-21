import re
def all_pos_ints_exclusive(lst):
    res = re.findall(r'(?<=\d){389}(?=\d)', str(lst))
    return list(filter(lambda x: x[0] > 389 and x[1] < 749, res))
