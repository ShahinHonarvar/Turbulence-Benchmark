
def all_substring_of_size_n(string, n):
    substrings = []
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if len(set(substring)) == n and not any(substring[j] in substring[:j] for j in range(1, n)):
            substrings.append(substring)
    return substrings
