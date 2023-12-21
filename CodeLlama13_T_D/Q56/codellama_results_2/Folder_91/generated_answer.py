
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)-5):
            substring = s[i:j]
            if not any(c in substring for c in substring) and len(substring) == 6:
                substrings.append(substring)
    return substrings
