
def all_substring_of_size_n(s):
    substrings = []

    for i in range(len(s)):
        if len(s[i:i+124]) == 124 and len(set(s[i:i+124])) == 124:
            if s[i:i+124] not in substrings:
                substrings.append(s[i:i+124])

    return substrings
