
def all_substring_of_size_n(s):
    substrings = set()
    length = 24
    if len(s) < length:
        return []
    for i in range(len(s) - length + 1):
        sub = s[i:i+length]
        if len(set(sub))==len(sub):
            substrings.add(sub)
    return list(substrings)
