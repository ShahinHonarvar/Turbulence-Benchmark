
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 45 + 1):
        substring = s[i:i+45]
        if len(set(substring)) == 45 and not any(c in substring for c in substrings):
            substrings.append(substring)
    return substrings
