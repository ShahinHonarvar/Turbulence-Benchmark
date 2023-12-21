
def all_substring_of_size_n(string):
    substrings = set()
    if len(string) < 40:
        return []
    for i in range(len(string) - 39):
        sub = string[i:i+40]
        if len(set(sub)) == len(sub):
            substrings.add(sub)
    return list(substrings)
