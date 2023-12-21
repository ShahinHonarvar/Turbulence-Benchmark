import re
def all_substring_of_size_n(s):
    if len(s) < 10 ** 5:
        return []
    m = re.match(r'(.{10 ** 5})', s)
    if m is None:
        return []
    return m.group(1).split()
