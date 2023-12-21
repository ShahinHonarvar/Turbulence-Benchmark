
def all_substring_of_size_n(s):
    length = len(s)
    if length < 17:
        return []
    substrings = set()
    for i in range(length - 16):
        substring = s[i:i+17]
        if len(set(substring)) == 17:
            substrings.add(substring)
    return list(substrings)
