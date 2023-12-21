
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 30 + 1):
        substr = s[i:i+30]
        if len(substr) == 30 and not any(c in substr for c in substrings):
            substrings.append(substr)
    return substrings
