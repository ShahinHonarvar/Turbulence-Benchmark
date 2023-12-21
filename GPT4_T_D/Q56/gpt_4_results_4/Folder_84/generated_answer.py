
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        if len(s[i:i+114]) == 114:
            if len(set(s[i:i+114])) == 114:
                if s[i:i+114] not in substrings:
                    substrings.append(s[i:i+114])
    return substrings
