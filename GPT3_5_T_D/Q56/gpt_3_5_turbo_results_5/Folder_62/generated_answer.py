
def all_substring_of_size_n(string):
    substrings = []

    if len(string) < 32:
        return []

    for i in range(len(string) - 31):
        substring = string[i:i+32]
        if len(set(substring)) == len(substring):
            substrings.append(substring)

    return substrings
