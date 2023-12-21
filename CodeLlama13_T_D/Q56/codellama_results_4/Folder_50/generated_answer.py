
def all_substring_of_size_n(string, n):
    substrings = []
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substring = string[i:j]
            if len(substring) == n and not any(substring in s for s in substrings):
                substrings.append(substring)
    return substrings
