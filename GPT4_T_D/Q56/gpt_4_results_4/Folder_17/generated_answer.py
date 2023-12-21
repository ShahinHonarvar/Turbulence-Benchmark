
def all_substring_of_size_n(string):
    substring_list = []
    for i in range(len(string)-36):
        substring = string[i:i+37]
        if len(set(substring)) == 37:
            if substring not in substring_list:
                substring_list.append(substring)
    return substring_list
