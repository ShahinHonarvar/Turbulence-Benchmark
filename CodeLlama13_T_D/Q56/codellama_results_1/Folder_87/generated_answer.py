
def all_substring_of_size_n(string, n):
    substrings = []
    for i in range(len(string)):
        for j in range(i+1, len(string)-n+1):
            substring = string[i:j]
            if len(set(substring)) == n and substring not in substrings:
                substrings.append(substring)
    return substrings
