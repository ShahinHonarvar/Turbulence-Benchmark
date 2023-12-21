
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 30 + 1):
        substring = s[i:i+30]
        if len(set(substring)) == 30 and len(substring) == 30:
            substrings.append(substring)
    return substrings
