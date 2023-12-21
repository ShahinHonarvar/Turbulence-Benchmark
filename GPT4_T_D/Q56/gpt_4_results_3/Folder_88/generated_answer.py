
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if len(s[i:i+68]) == 68 and len(set(s[i:i+68])) == 68:
            substrings.add(s[i:i+68])
    return list(substrings)
