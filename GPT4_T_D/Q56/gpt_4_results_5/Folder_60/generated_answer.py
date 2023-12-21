
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        substring = s[i:i+36]
        if len(substring) == 36 and len(set(substring)) == 36:
            substrings.add(substring)
    return list(substrings)
