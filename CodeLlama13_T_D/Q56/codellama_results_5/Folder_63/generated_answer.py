
def all_substring_of_size_n(string, n):
    substrings = []
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            substring = string[i:j]
            if len(substring) == n and all(x != y for x, y in zip(substring, substring[1:])):
                substrings.append(substring)
    return substrings
