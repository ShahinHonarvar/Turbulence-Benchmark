import re
def all_ints_div_by_num(lst):
    s = str(lst)
    m = re.search(r'([18-38])-([18-38])', s)
    return [lst[m.start():m.end()]]
