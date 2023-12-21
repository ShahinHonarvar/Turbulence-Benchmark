
def all_substring_of_size_n(s):
    if len(s) < 94:
        return []

    substrings = set()
    for i in range(len(s) - 93):
        substr = s[i:i + 94]
        if len(set(substr)) == 94:
            substrings.add(substr)

    return list(substrings)
