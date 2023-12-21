
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 10 + 1):
        substring = s[i:i+10]
        if len(set(substring)) == 10 and not any(substring.startswith(x) for x in substrings):
            substrings.append(substring)
    return substrings
