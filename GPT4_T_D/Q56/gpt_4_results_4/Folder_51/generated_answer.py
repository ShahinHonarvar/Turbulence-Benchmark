
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if i + 96 <= len(s):
            substring = s[i:i+96]
            if len(set(substring)) == 96:
                substrings.add(substring)
    return list(substrings)
