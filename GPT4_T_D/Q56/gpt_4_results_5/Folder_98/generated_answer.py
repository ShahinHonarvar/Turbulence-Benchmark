
def all_substring_of_size_n(s):
    substrings = []
    for i in range(0, len(s) - 9):
        substring = s[i:i + 10]
        if len(set(substring)) == 10:
            substrings.append(substring)
    return list(set(substrings))
