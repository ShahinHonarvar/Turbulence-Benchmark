
def all_substring_of_size_n(s):
    substrings = set()
    length = len(s)
    for i in range(length):
        if i + 26 <= length:
            substring = s[i:i+26]
            if len(set(substring)) == 26:
                substrings.add(substring)
    return list(substrings)
