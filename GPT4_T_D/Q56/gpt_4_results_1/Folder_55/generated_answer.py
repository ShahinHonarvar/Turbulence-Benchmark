
def all_substring_of_size_n(s):
    all_substrings = []
    for i in range(len(s)-39):
        substring = s[i:i+40]
        if len(substring) == len(set(substring)):
            if substring not in all_substrings:
                all_substrings.append(substring)
    return all_substrings
