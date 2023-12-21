
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)-57):
            substring = s[i:j]
            if not any(substring in sub for sub in substrings) and not any(char in substring for char in set(substring)):
                substrings.append(substring)
    return substrings
