
def all_substring_of_size_n(s):
    subs = set()
    for i in range(len(s)):
        if len(s[i:i+17]) == 17 and len(set(s[i:i+17])) == 17:
            subs.add(s[i:i+17])
    return list(subs)
