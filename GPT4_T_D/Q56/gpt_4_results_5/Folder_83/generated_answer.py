
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 47):
        substring = s[i:i+48]
        if len(set(substring)) == 48:
            if substring not in substrings:
                substrings.append(substring)
    return substrings
