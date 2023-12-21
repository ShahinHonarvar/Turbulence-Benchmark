
def all_substring_of_size_n(s):
    n = 2
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring not in substrings and len(set(substring)) == n:
            substrings.append(substring)
    return substrings
