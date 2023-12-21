
def all_substring_of_size_n(s):
    substring_set = set()
    for i in range(len(s) - 66):
        substring = s[i:i+67]
        if len(set(substring)) == len(substring):
            substring_set.add(substring)
    return list(substring_set)
