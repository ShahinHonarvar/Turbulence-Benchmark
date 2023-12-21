
def all_substring_of_size_n(s):
    substrings = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 44, min(length + 1, i + 45)):
            substring = s[i:j]
            if len(set(substring)) == len(substring):
                substrings.add(substring)
    return list(substrings)
