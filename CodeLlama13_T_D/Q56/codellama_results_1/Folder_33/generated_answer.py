
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if len(substring) == 105 and not any(substring[k] == substring[k-1] for k in range(2, len(substring))):
                substrings.append(substring)
    return list(set(substrings))
