
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 98 + 1):
        substring = string[i:i+98]
        if len(set(substring)) == 98 and not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
