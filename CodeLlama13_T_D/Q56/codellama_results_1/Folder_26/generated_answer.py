
def all_substring_of_size_n(s):
    subs = []
    for i in range(len(s)):
        sub = s[i:i+33]
        if len(set(sub)) == 33 and not any(sub in subs for sub in subs):
            subs.append(sub)
    return subs
