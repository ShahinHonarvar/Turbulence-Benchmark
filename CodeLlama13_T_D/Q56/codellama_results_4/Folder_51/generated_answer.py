
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 96 + 1):
        substring = s[i:i+96]
        if not any(c in substring for c in substrings):
            substrings.append(substring)
    return substrings
