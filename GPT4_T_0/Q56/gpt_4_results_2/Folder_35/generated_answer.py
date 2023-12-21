
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 26):
        substring = s[i:i+27]
        if len(set(substring)) == 27:
            substrings.add(substring)
    return list(substrings)
