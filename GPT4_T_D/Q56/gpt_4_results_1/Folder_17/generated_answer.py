
def all_substring_of_size_n(s):
    length = 37
    substrings = set()
    for i in range(len(s)):
        substring = s[i:i+length]
        if len(substring) == length and len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)
