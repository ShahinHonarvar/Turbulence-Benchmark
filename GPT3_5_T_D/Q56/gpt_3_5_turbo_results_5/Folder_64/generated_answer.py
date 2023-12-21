
def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string)-7):
        substring = string[i:i+8]
        if len(set(substring)) == 8:
            substrings.add(substring)
    return list(substrings)
