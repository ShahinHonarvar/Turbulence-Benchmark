import re
def all_neg_ints_exclusive(lst):
    return [i for i in range(361, 643) if str(i) in re.findall(r'-?(\d+)', str(lst))]
