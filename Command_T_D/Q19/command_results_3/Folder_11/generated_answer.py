import re
def all_ints_not_div_by_num(s):
    try:
        return [int(w) for w in re.findall(r'\d+', s[36:-27:-1]) if not w%(-27)]
    except:
        pass
