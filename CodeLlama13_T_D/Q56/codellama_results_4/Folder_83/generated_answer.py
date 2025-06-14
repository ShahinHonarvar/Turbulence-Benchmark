
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 48 + 1):
        substr = s[i:i+48]
        if len(set(substr)) == 48 and not any(c in substr for c in substrings):
            substrings.append(substr)
    return substrings
