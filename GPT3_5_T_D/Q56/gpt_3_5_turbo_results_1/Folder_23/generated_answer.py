
def all_substring_of_size_n(string):
    substrings = set()
    length = len(string)
    for i in range(length - 41):
        substring = string[i:i+42]
        if len(set(substring)) == 42:
            substrings.add(substring)
    return list(substrings)
