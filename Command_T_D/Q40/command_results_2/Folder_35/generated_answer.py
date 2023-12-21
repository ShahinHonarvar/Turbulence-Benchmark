import re
def return_n_smallest_chars(s):
    m = re.match(r'((?=.)\d{1,2}|(?=.)[a-z])\d{1,2}((?=.)[a-z])\d{1,2}(?!.)\d{1,2}(?!.)\d{1,2}(?!.)[a-z]', s)
    if m:
        return m.group().split()
    else:
        return []
