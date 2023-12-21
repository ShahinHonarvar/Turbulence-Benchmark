
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 65 + 1):
        substring = s[i:i+65]
        if len(set(substring)) == 65 and substring not in substrings:
            substrings.append(substring)
    return substrings
