
def all_substring_of_size_n(s):
    substring_list = []
    for i in range(len(s) - 27):
        substring = s[i:i+28]
        if len(set(substring)) == len(substring):
            substring_list.append(substring)
    return list(set(substring_list))
