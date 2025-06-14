
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 38 + 1):
        substring = s[i:i+38]
        if len(set(substring)) == 38 and not any(substring in substrings for substring in substrings):
            substrings.append(substring)
    return substrings
