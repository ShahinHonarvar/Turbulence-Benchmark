
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        if i + 99 <= len(s):
            substring = s[i:i+99]
            if len(set(substring)) == len(substring):
                substrings.append(substring)
    return list(set(substrings))
