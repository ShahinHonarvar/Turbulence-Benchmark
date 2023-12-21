
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        end = i + 37
        if end > len(s):
            break
        substring = s[i:end]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)
