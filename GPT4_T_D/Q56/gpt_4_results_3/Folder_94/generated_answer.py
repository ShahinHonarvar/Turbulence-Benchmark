
def all_substring_of_size_n(s):
    substring_list = []
    for i in range(len(s) - 69):
        substring = s[i:i + 70]
        if len(substring) == len(set(substring)):
            substring_list.append(substring)
    return list(set(substring_list))
