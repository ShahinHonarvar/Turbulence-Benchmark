
def all_substring_of_size_n(s):
    l = len(s)
    substrings = set()
    for i in range(l):
        for j in range(i + 29, min(i + 60, l + 1)):
            sub = s[i:j]
            if len(set(sub)) == len(sub):
                substrings.add(sub)
    return [sub for sub in substrings if len(sub) == 29]
