
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        if len(s[i:i+85]) == 85 and len(set(s[i:i+85])) == 85:
            if s[i:i+85] not in substrings:
                substrings.append(s[i:i+85])
    return substrings
