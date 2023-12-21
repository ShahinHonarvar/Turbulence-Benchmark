
def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if len(substring) == 54 and len(set(substring)) == len(substring):
                substrings.add(substring)
    return list(substrings)
