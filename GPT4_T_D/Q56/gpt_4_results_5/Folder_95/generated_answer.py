
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        if i + 89 <= len(s):
            substring = s[i:i+89]
            if len(set(substring)) == len(substring):
                substrings.append(substring)
    return list(set(substrings))
