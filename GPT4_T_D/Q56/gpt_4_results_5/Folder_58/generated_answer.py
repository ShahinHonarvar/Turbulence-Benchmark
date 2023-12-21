
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if len(s[i:i+127]) == 127 and len(set(s[i:i+127])) == 127:
            substrings.add(s[i:i+127])
    return list(substrings)
