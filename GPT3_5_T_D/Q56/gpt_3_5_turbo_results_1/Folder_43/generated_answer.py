

def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string)-85):
        substring = string[i:i+86]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)
