
def all_substring_of_size_n(string, n):
    substrings = []
    for i in range(len(string)):
        for j in range(i+1, len(string)-n+2):
            substring = string[i:j]
            if not any(substring in s for s in substrings) and len(set(substring)) == n:
                substrings.append(substring)
    return substrings
