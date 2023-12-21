
def all_substring_of_size_n(string):
    substrings = set()
    n = len(string)
    for i in range(n - 59):
        sub = string[i:i + 60]
        if len(set(sub)) == len(sub):
            substrings.add(sub)
    return list(substrings)
