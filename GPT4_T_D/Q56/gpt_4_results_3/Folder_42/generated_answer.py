
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        substring = s[i:i+45]
        if len(substring) == 45 and len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)
