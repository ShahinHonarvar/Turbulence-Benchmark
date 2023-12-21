
def all_substring_of_size_n(s):
    subs = set()
    if len(s) < 79:
        return []
    for i in range(len(s) - 78):
        substring = s[i:i+79]
        if len(set(substring)) == 79:
            subs.add(substring)
    return list(subs)
