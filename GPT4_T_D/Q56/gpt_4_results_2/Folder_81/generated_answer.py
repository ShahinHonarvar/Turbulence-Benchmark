
def all_substring_of_size_n(s):
    all_substrs = set()
    for i in range(len(s)):
        if i + 98 <= len(s) and len(set(s[i:i+98])) == 98:
            all_substrs.add(s[i:i+98])
    return list(all_substrs)
