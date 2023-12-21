import re
def return_n_smallest_chars(s):
    # find distinct characters
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    # sort by ASCII value
    m = re.findall("[A-Z]", s)
    m.sort(key=lambda x: ord(x))
    return m[:38]
