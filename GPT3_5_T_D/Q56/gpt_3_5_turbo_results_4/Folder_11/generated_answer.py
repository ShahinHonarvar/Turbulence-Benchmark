
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)-77):
        substring = string[i:i+78]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings
