
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 87):
        substring = s[i:i+88]
        if len(substring) == len(set(substring)):
            substrings.append(substring)

    return list(set(substrings))
