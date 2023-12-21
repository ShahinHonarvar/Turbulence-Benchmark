
def all_substring_of_size_n(string):
    substring_set = set()
    for i in range(len(string)-85):
        substring = string[i:i+86]
        if len(set(substring)) == 86:
            substring_set.add(substring)
    return list(substring_set)
