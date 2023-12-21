
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 98):
        substring = s[i:i+99]
        if len(set(substring)) == 99 and not any(substring in sub for sub in substrings):
            substrings.append(substring)
    return substrings
