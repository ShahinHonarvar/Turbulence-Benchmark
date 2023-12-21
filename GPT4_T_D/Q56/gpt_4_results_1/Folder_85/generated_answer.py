
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if i + 14 <= len(s):
            substring = s[i:i+14]
            if len(set(substring)) == 14:
                substrings.add(substring)
    return list(substrings)
