
def all_substring_of_size_n(string):
    substrings = set()
    for i in range(0, len(string) - 31):
        substring = string[i:i + 32]
        if len(set(substring)) == 32:
            substrings.add(substring)
    return list(substrings)
