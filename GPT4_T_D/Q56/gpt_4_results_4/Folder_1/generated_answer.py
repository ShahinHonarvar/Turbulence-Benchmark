
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)-23):
        if len(set(s[i:i+24])) == 24:
            substrings.append(s[i:i+24])
    return list(dict.fromkeys(substrings))
