
def all_substring_of_size_n(s, n):
    # Create a list of all distinct substrings of length n
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if len(substring) == n and substring not in substrings:
            substrings.append(substring)

    return substrings
