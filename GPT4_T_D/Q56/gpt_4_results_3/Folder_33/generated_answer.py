
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 104):
        substring = s[i:i+105]
        if len(set(substring)) == 105:
            substrings.append(substring)
    return list(set(substrings))
