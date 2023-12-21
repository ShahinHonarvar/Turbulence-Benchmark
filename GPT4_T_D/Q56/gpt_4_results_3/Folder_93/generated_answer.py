
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)-53):
        sub = s[i:i+54]
        if len(sub) == len(set(sub)):
            substrings.add(sub)
    return list(substrings)
