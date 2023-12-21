
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 10):
        substring = string[i:i+11]
        if len(set(substring)) == 11 and not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
