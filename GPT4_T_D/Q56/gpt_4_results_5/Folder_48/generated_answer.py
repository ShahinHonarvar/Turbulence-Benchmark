
def all_substring_of_size_n(s):
    substrings = set()
    length = len(s)

    for i in range(length):
        for j in range(i + 120, length + 1):
            substr = s[i:j]
            if len(set(substr)) == len(substr):
                substrings.add(substr)
    return list(substrings)
