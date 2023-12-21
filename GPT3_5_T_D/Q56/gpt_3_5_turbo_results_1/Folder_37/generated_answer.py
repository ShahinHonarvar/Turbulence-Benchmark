
def all_substring_of_size_n(string):
    n = 65
    substrings = []
    for i in range(len(string)-n+1):
        substring = string[i:i+n]
        if len(set(substring)) == n:
            substrings.append(substring)
    return substrings
