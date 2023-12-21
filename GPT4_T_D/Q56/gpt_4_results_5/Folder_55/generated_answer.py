
def all_substring_of_size_n(s):
    if len(s) < 40:
        return []
    else:
        substring_list = []
        for i in range(len(s) - 40 + 1):
            substring = s[i:i+40]
            if len(set(substring)) == len(substring):
                if substring not in substring_list:
                    substring_list.append(substring)
        return substring_list
