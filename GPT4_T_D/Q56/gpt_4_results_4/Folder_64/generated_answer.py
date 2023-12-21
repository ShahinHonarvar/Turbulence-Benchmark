
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if len(s[i:i+8]) == 8 and len(set(s[i:i+8])) == 8:
            substrings.add(s[i:i+8])
    return list(substrings)
