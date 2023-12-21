
def all_substring_of_size_n(s):
    substring_list = []
    for i in range(len(s) - 11):
        substring = s[i:i + 12]
        if len(substring) == 12 and len(set(substring)) == 12:
            if substring not in substring_list:
                substring_list.append(substring)
    return substring_list
