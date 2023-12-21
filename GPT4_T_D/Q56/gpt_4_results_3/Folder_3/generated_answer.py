
def all_substring_of_size_n(s):
    size = 93
    length = len(s)
    if size > length:
        return []
    result = set()
    for i in range(length - size + 1):
        substring = s[i:i + size]
        if len(substring) == len(set(substring)):
            result.add(substring)
    return list(result)
