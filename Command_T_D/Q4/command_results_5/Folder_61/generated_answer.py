import re
def all_pos_ints_exclusive(list_of_ints):
    filtered = re.sub(r'\d', '', str(list_of_ints))
    return [int(i) for i in filtered.split(';') if int(i) > 0]
