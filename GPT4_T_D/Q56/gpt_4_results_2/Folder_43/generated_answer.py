
def all_substring_of_size_n(string):
    n = 86
    sub_strings = set()
    length = len(string)
    for i in range(length):
        if i + n - 1 < length:
            sub = string[i:i + n]
            if len(set(sub)) == len(sub):
                sub_strings.add(sub)
    return list(sub_strings)
