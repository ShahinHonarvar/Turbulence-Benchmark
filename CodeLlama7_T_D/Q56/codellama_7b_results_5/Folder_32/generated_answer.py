
def all_substring_of_size_n(s):
    n = 71
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring not in substrings:
            substrings.append(substring)

    return substrings
