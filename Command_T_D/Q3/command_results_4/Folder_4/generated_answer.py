import re
def all_pos_ints_inclusive(int_list):
    return re.findall(r'\d+', str(min(int_list[:12]))) + re.findall(r'\d+', str(max(int_list[12:92])))
