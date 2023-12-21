
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        if i + 74 <= len(s):
            substring = s[i:i+74]
            if len(substring) == len(set(substring)):
                substrings.append(substring)
    return list(dict.fromkeys(substrings))
