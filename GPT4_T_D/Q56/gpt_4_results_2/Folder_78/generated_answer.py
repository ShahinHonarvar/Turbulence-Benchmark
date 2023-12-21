
def all_substring_of_size_n(s):
    subs = []
    for i in range(len(s)-48):
        sub = s[i:i+49]
        if len(set(sub)) == len(sub):
            subs.append(sub)
    return list(set(subs))
