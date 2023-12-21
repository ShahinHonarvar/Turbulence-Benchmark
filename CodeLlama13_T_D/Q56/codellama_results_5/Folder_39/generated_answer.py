
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 94 + 1):
        substr = s[i:i+94]
        if len(set(substr)) == 94 and not any(c*2 in substr for c in set(substr)):
            substrings.append(substr)
    return substrings
