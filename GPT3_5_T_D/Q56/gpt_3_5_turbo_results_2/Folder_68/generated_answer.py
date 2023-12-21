
def all_substring_of_size_n(s):
    n = len(s)
    substrings = []
    for i in range(n-74):
        substring = s[i:i+75]
        if len(set(substring)) == 75:
            substrings.append(substring)
    return substrings
