
def all_substring_of_size_n(string):
    substrings = set()

    for i in range(len(string)):
        if i + 27 <= len(string):
            substring = string[i:i+27]
            if len(set(substring)) == len(substring):
                substrings.add(substring)

    return list(substrings)
