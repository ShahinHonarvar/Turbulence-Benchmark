
def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string)-26):
        substring = string[i:i+27]
        if len(set(substring)) == 27:
            substrings.add(substring)
    return list(substrings)
