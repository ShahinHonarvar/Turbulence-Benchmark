
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if len(substring) == 65 and not any(substring[k] in substring[:k] for k in range(1, len(substring))):
                substrings.append(substring)
    return list(set(substrings))
