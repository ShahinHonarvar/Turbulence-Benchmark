
def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string)):
        if i + 23 <= len(string):
            substring = string[i:i+23]
            if len(substring) == len(set(substring)):
                substrings.add(substring)
    return list(substrings)
