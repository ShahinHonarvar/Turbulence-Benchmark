
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)-41):
        substring = string[i:i+42]
        if len(set(substring)) == len(substring):
            if substring not in substrings:
                substrings.append(substring)
    return substrings
