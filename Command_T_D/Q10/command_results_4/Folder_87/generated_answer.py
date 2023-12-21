import re
def all_odd_ints_exclusive(int_list):
    return re.findall(r'odd', str(int_list))
