
def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string)):
        if i + 19 > len(string):
            break
        substring = string[i:i+19]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)
