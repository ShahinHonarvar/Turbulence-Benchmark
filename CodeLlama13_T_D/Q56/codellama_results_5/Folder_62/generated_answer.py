
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 31):
        substr = s[i:i+32]
        if len(set(substr)) == 32 and len(substr) == 32:
            substrings.append(substr)
    return substrings
