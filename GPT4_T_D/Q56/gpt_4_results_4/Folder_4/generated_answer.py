
def all_substring_of_size_n(s):
    length = 41
    substrings = []
    for i in range(len(s) - length + 1):
        substring = s[i : i+length]
        if len(set(substring)) == length:
            if substring not in substrings:
                substrings.append(substring)
    return substrings
