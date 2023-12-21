
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if len(substring) == 47 and all(c not in substring for c in substring[:-1]):
                substrings.append(substring)
    return list(set(substrings))
