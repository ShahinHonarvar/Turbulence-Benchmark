
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 148):
        substring = string[i:i+149]
        if len(set(substring)) == 149 and all(c not in substrings for c in substring):
            substrings.append(substring)
    return substrings
