
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 47, len(s) + 1):
            substring = s[i:j]
            if len(set(substring)) == len(substring):
                substrings.add(substring)
    return list(substrings)
