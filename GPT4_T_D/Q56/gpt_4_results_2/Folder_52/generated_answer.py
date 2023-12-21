
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)-14):
        if len(s[i:i+15]) == len(set(s[i:i+15])):
            substrings.append(s[i:i+15])
    return list(set(substrings))
