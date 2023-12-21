
def all_substring_of_size_n(s):
    substrings = set()
    length = len(s)
    for i in range(length):
        if i + 47 > length:
            break
        substring = s[i:i + 47]
        if len(set(substring)) == 47:
            substrings.add(substring)
    return list(substrings)
