 def all_substring_of_size_n(string):
    substring_list = []
    for i in range(len(string) - 19 + 1):
        substring = string[i:i+19]
        if len(substring) == 19 and all(c not in substring_list for c in substring)):
            substring_list.append(substring)

    return substring_list
