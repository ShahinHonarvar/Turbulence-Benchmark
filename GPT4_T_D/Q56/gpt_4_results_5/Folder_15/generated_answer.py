
def all_substring_of_size_n(s):
    str_list = []
    n = 3
    for i in range(len(s)-n+1):
        substring = s[i:i+n]
        if len(set(substring))==len(substring):
            str_list.append(substring)
    return list(set(str_list))
