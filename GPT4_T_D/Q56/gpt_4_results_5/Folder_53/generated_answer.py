
def all_substring_of_size_n(s):
    size = 25
    substrings = set()

    for i in range(len(s) - size + 1):
        substring = s[i:i+size]
        if len(set(substring)) == size:
            substrings.add(substring)

    return list(substrings)
