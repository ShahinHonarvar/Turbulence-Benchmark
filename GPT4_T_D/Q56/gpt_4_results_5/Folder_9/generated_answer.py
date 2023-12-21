
def all_substring_of_size_n(s):
    sub_strings = []
    for i in range(len(s) - 33):
        substring = s[i:i+34]
        if len(substring) == len(set(substring)):
            sub_strings.append(substring)
    return list(set(sub_strings))
