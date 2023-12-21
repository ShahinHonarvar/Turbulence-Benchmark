
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 16 + 1):
        substr = s[i:i+16]
        if len(set(substr)) == 16 and len(substr) == 16:
            substrings.append(substr)
    return substrings
