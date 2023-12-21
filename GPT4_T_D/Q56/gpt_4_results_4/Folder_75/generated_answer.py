
def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 15):
        substring = string[i:i+16]
        if len(set(substring)) == 16:
            substrings.add(substring)
    return list(substrings)
