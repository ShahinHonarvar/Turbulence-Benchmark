
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if len(substring) == 142 and all_unique_chars(substring):
                substrings.append(substring)
    return substrings
