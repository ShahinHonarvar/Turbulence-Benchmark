
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)-14):
            substring = s[i:j]
            if len(substring) == 15 and all(substring[i] != substring[j] for i in range(15)):
                substrings.append(substring)
    return list(set(substrings))
