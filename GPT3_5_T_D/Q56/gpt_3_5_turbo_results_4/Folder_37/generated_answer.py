
def all_substring_of_size_n(string):
    substrings = set()
    length = len(string)
    if length < 65:
        return []

    for i in range(length - 64):
        substring = string[i:i+65]
        if len(set(substring)) == len(substring):
            substrings.add(substring)

    return list(substrings)
