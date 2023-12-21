
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 51):
        substr = s[i:i+52]
        if len(set(substr)) == 52 and substr not in substrings:
            substrings.append(substr)
    return substrings
