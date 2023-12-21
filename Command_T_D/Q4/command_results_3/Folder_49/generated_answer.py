import re
def all_pos_ints_exclusive(ints):
    if not ints:
        return []
    return [int(i) for i in re.findall(r'\d+', f'{ints[80]:d}<{ints[200]:d}')]
