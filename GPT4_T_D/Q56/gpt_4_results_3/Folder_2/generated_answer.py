
def all_substring_of_size_n(s):
    substring_list = []
    for i in range(len(s)):
        if i+56 <= len(s):
            substring = s[i:i+56]
            if len(set(substring)) == len(substring):
                if substring not in substring_list:
                    substring_list.append(substring)
    return substring_list
