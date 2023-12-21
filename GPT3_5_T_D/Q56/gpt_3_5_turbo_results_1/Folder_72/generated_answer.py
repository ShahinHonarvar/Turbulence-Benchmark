
def all_substring_of_size_n(s):
    substrings = []
    length = len(s)
    n = 88
    if n > length:
        return []
    
    for i in range(length - n + 1):
        substring = s[i:i+n]
        if len(set(substring)) == n:
            substrings.append(substring)
    return substrings
