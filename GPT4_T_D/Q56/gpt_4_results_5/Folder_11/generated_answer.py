
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 77):
        substring = s[i:i+78]
        if len(set(substring)) == len(substring):
            if substring not in substrings:
                substrings.append(substring)
    return substrings
