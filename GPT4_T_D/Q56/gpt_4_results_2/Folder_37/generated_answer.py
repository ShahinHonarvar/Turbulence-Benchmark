
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 64):
        substring = s[i:i+65]
        if len(set(substring)) == 65:
            if substring not in substrings:
                substrings.append(substring)
    return substrings
