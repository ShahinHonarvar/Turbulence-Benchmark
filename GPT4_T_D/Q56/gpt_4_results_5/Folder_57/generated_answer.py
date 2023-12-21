
def all_substring_of_size_n(s):
    substrs = set()
    for i in range(len(s) - 59):
        substr = s[i:i + 60]
        if len(set(substr)) == 60:
            substrs.add(substr)
    return list(substrs)
