
def all_substring_of_size_n(string):
    substring_list = []
    for i in range(len(string)-20):
        substring = string[i:i+21]
        if len(set(substring)) == len(substring):
            if substring not in substring_list:
                substring_list.append(substring)
    return substring_list
