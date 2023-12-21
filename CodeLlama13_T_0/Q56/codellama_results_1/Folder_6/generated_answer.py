
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 23 + 1):
        substring = s[i:i+23]
        if len(set(substring)) == 23 and not any(substring in substrings for substring in substrings):
            substrings.append(substring)
    return substrings
