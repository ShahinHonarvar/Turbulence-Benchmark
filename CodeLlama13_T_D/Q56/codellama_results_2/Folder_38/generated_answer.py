
def all_substring_of_size_n(string, n):
    substrings = []
    for i in range(len(string)):
        substring = string[i:i+n]
        if len(set(substring)) == n and not any(substring in s for s in substrings):
            substrings.append(substring)
    return substrings
