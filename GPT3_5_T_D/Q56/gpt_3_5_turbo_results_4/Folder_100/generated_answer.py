
def all_substring_of_size_n(string):
    if len(string) < 92:
        return []

    substrings = set()
    for i in range(len(string)-91):
        substring = string[i:i+92]
        if len(set(substring)) == len(substring):
            substrings.add(substring)

    return list(substrings)
