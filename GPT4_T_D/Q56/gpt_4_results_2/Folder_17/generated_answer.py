
def all_substring_of_size_n(s):
    substring_list = []
    for i in range(len(s) - 36):
        substring = s[i:i+37]
        if len(set(substring)) == 37:
            if substring not in substring_list:
                substring_list.append(substring)
    return substring_list
