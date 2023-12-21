
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 104):
        substring = s[i:i+105]
        if len(set(substring)) == 105:
            substrings.add(substring)
    return list(substrings)
