
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if len(substring) == 97 and not any(c in substring for c in substrings):
                substrings.append(substring)
    return substrings
