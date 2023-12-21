
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 127 + 1):
        substring = s[i:i+127]
        if len(set(substring)) == 127 and all([x not in substring for x in substring]):
            substrings.append(substring)
    return substrings
