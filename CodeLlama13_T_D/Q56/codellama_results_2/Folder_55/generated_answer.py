
def all_substring_of_size_n(s):
    subs = []
    for i in range(len(s)-39):
        sub = s[i:i+40]
        if len(set(sub)) == 40 and all(c not in subs for c in sub):
            subs.append(sub)
    return subs
