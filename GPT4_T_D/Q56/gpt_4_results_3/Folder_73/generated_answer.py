
def all_substring_of_size_n(s):
    substring_list = []
    for i in range(len(s) - 19):
        substring = s[i:i+20]
        if len(set(substring)) == len(substring):
            if substring not in substring_list:
                substring_list.append(substring)
    return substring_list
