
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 73 + 1):
        substring = s[i:i+73]
        if len(set(substring)) == 73 and substring not in substrings:
            substrings.append(substring)
    return substrings
