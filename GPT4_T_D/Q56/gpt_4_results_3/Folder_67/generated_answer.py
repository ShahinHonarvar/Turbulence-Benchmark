
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        if i + 43 > len(s):
            break
        substring = s[i:i+43]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return list(set(substrings))
