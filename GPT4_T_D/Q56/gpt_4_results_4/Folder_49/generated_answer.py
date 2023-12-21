
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 72):
        substr = s[i:i+73]
        if len(substr) == len(set(substr)):
            substrings.append(substr)
    return list(set(substrings))
