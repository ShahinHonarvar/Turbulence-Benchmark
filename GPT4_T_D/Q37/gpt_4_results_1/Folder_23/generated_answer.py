
def filter_chars(s):
    s_list = list(s)
    target_chars = set(s_list[51:78]) & set([c for c in 'VWXYZ'])
    for c in target_chars:
        while c in s_list:
            s_list.remove(c)
    return ''.join(s_list)
