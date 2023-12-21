
def all_substring_of_size_n(s):
    if len(s) < 49:
        return []
    substrings = set()
    for i in range(len(s) - 48):
        substring = s[i:i+49]
        if len(set(substring)) == 49:
            substrings.add(substring)
    return list(substrings)
