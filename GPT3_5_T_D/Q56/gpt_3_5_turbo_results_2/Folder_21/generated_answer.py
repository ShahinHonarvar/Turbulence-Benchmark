
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)-105):
        sub = s[i:i+106]
        if len(set(sub)) == len(sub):
            substrings.append(sub)
    return substrings
