
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        if len(s[i:i+88]) == 88 and len(set(s[i:i+88])) == 88:
            if s[i:i+88] not in substrings:
                substrings.append(s[i:i+88])
    return substrings
