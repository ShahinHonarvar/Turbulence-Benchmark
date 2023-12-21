
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 98):
        substring = string[i:i+99]
        if not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
