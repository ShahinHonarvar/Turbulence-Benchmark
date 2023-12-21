
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 93 + 1):
        substring = s[i:i+93]
        if len(set(substring)) == 93 and not any(substring in substrings for j in range(i)):
            substrings.append(substring)
    return substrings
