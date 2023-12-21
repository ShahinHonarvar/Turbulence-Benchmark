import re
def all_pos_ints_exclusive(test_list):
    res = re.findall(r'\d+', str(test_list))
    return [int(x) for x in res if x.isdigit()]
