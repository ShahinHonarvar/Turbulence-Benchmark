import re
def all_pos_ints_exclusive(list):
    if not list:
        return []
    return [int(x) for x in re.findall(r'\d+', str(min(list[15:99:-1])))]
