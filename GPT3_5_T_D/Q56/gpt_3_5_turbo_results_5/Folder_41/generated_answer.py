
def all_substring_of_size_n(s):
    substrings = []
    n = len(s)
    for i in range(n-73):
        substring = s[i:i+74]
        if len(set(substring)) == 74:
            substrings.append(substring)
    return substrings
