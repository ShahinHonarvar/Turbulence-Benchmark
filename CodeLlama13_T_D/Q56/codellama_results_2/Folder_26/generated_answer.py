
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i, len(s) - 32):
            substring = s[i:j + 1]
            if len(set(substring)) == 33 and all_distinct(substring):
                substrings.append(substring)
    return substrings
