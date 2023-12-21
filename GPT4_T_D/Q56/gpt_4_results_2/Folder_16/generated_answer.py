
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        substring = s[i: i + 124]
        if len(substring) == 124 and len(set(substring)) == 124:
            if substring not in substrings:
                substrings.append(substring)
    return substrings
