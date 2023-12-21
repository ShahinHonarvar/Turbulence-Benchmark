
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 19):
        substring = s[i:i+20]
        if len(set(substring)) == 20 and not any(substring in substrings for substrings in substrings):
            substrings.append(substring)
    return substrings
