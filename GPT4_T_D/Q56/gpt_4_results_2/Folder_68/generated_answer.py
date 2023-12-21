
def all_substring_of_size_n(s):
    subs = set()
    for i in range(len(s)):
        if len(set(s[i:i+75])) == 75:
            subs.add(s[i:i+75])
    return list(subs)
