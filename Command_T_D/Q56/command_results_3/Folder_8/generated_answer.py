def all_substring_of_size_n(s):
    if not s:
        return []
    lst = []
    for i in range(len(s) - 29):
        lst += [s[i:i + 30]]
    return lst
