import re
def all_ints_div_by_num(lst):
    s = re.sub(r'[a-z]','',str(lst))
    return [int(x) for x in lst[25:-1] if int(x) % -97 == 0]
