
def all_substring_of_size_n(s):
    subs = set()
    for i in range(len(s)):
        if len(set(s[i:i+94])) == 94:
            subs.add(s[i:i+94])
    return list(subs)
