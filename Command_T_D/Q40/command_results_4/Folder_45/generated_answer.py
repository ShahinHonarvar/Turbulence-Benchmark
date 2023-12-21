import re
def return_n_smallest_chars(s):
    res = []
    for c in sorted(re.findall(r'[a-z]', s), key=lambda x: ord(x)):
        res.append(c)
        if len(res) == 52:
            break
    return res
