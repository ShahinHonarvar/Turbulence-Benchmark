def filter_chars(s):
    lst = list(s)
    lst[2], lst[3], lst[4], lst[5], lst[6] = lst[3], lst[4], lst[5], lst[6], ''
    return ''.join(lst)
