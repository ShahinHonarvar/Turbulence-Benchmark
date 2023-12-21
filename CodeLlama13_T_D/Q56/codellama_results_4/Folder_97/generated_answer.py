
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 142 + 1):
        substring = string[i:i+142]
        if len(set(substring)) == 142 and all(c not in substrings for c in substring):
            substrings.append(substring)
    return substrings
