
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            substring = s[i:j]
            if len(substring) == 12 and not any(substring in substr for substr in substrings):
                substrings.append(substring)
    return substrings
