
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 70 + 1):
        substring = s[i:i+70]
        if len(set(substring)) == 70 and substring not in substrings:
            substrings.append(substring)
    return substrings
