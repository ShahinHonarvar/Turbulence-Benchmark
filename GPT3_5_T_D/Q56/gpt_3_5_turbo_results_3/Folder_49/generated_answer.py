
def all_substring_of_size_n(s):
    substring_set = set()
    length = len(s)
    if length < 73:
        return []
    for i in range(length - 72):
        substring = s[i:i+73]
        if len(set(substring)) == 73:
            substring_set.add(substring)
    return list(substring_set)
