
def all_substring_of_size_n(string):
    n = 88
    substrings = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)
