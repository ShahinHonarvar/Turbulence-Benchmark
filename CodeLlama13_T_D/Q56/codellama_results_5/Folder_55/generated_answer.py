
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 40 + 1):
        substring = s[i:i+40]
        if len(set(substring)) == 40 and not any(substring in ss for ss in substrings):
            substrings.append(substring)
    return substrings
