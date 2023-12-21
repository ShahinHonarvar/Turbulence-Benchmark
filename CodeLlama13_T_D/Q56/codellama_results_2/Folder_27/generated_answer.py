
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 57 + 1):
        substring = s[i:i+57]
        if len(set(substring)) == 57 and len(substring) == 57:
            substrings.append(substring)
    return substrings
