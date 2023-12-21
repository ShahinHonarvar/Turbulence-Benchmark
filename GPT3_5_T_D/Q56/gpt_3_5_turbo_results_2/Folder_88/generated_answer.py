
def all_substring_of_size_n(string):
    substrings = set()
    if len(string) < 68:
        return []
    for i in range(len(string)-67):
        substring = string[i:i+68]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)
