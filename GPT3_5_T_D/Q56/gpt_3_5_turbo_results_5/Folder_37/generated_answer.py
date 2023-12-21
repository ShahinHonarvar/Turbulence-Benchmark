
def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 64):
        substring = string[i:i+65]
        if len(set(substring)) == 65:
            substrings.add(substring)
    return list(substrings)
