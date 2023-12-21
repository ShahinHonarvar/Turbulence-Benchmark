
def all_substring_of_size_n(string):
    substrings = []
    n = 78
    for i in range(len(string) - n + 1):
        sub = string[i:i+n]
        if len(set(sub)) == len(sub):
            substrings.append(sub)
    return substrings
