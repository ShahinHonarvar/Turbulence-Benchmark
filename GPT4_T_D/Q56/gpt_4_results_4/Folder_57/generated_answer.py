
def all_substring_of_size_n(s):
    substring_set = set()
    for i in range(len(s)):
        if len(s[i:i+60]) == 60 and len(set(s[i:i+60])) == 60:
            substring_set.add(s[i:i+60])
    return list(substring_set)
