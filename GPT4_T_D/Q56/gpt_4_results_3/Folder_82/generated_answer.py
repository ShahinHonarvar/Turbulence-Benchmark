
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 99):
        substring = s[i : i + 100]
        if len(set(substring)) == 100:
            if substring not in substrings:
                substrings.append(substring)
    return substrings
