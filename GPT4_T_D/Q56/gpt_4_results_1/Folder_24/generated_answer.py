
def all_substring_of_size_n(s):
    if len(s) < 52:
        return []
    result_set = set()
    for i in range(len(s) - 52 + 1):
        substring = s[i: i + 52]
        if len(set(substring)) == 52:
            result_set.add(substring)
    return list(result_set)
