
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 56 + 1):
        substring = string[i:i+56]
        if len(set(substring)) == 56 and not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
