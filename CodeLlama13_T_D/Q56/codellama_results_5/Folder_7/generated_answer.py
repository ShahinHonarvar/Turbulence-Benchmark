
def all_substring_of_size_117(string):
    substrings = []
    for i in range(len(string) - 116):
        substring = string[i:i+117]
        if len(set(substring)) == 117 and all(c not in substrings for c in substring):
            substrings.append(substring)
    return substrings
