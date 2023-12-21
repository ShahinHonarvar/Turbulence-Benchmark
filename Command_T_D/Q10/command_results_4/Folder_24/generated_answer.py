import re
def all_odd_ints_exclusive(lst):
    if not lst:
        return []
    indices = range(13, 66)
    return [e for e in lst if re.match(r"odd(-[0-9]+)", str(e))]
