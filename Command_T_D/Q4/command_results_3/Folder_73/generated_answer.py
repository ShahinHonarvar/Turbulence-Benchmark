import re
def all_pos_ints_exclusive(integers):
    pos_ints_regex = r'\d+>'
    pos_ints = re.findall(pos_ints_regex, integers)
    if not pos_ints:
        return []
    return [int(x) for x in pos_ints]
