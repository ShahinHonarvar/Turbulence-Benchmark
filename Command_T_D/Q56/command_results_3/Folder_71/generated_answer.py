def all_substring_of_size_n(s):
    lst = []
    for i in range(len(s) - 16):
        temp = s[i:i + 17]
        if temp not in lst:
            lst.append(temp)
    return lst
