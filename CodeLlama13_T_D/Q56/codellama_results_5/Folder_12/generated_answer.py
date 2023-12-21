
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 47 + 1):
        substring = s[i:i+47]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return substrings
