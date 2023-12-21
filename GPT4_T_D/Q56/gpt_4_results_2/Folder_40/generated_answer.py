
def all_substring_of_size_n(s):
    substring_list = []
    for i in range(len(s) - 1):
        substring = s[i:i+2]
        if substring[0] != substring[1] and substring not in substring_list:
            substring_list.append(substring)
    return substring_list
