
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        substr = s[i:i+54]
        if len(substr) == 54 and len(set(substr)) == 54:
            substrings.add(substr)
    return list(substrings)
